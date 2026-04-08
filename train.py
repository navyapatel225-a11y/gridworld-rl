import numpy as np
import random
from env import GridEnv

def train():
    num_states = 5
    num_actions = 2

    q_table = np.zeros((num_states, num_actions))

    alpha = 0.1
    gamma = 0.9
    epsilon = 0.2
    episodes = 500

    env = GridEnv()

    for _ in range(episodes):
        state = env.reset()
        done = False

        while not done:
            if random.uniform(0, 1) < epsilon:
                action = random.randint(0, num_actions - 1)
            else:
                action = int(np.argmax(q_table[state]))

            next_state, reward, done = env.step(action)

            q_table[state, action] = q_table[state, action] + alpha * (
                reward + gamma * np.max(q_table[next_state]) - q_table[state, action]
            )

            state = next_state

    return q_table
