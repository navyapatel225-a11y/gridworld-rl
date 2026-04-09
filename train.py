import numpy as np
from env import GridEnv

def train_q_learning():
    env = GridEnv()

    q_table = np.zeros((5, 2))
    alpha = 0.1
    gamma = 0.9
    epsilon = 0.1

    for _ in range(500):
        state = env.reset()
        done = False

        while not done:
            if np.random.rand() < epsilon:
                action = np.random.randint(2)
            else:
                action = np.argmax(q_table[state])

            next_state, reward, done = env.step(action)

            q_table[state, action] += alpha * (
                reward + gamma * np.max(q_table[next_state]) - q_table[state, action]
            )

            state = next_state

    return q_table
