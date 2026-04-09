import numpy as np
from env import GridEnv

def train_q_learning():
    env = GridEnv()
    q_table = np.zeros((5, 2))

    for _ in range(500):
        state = env.reset()
        done = False

        while not done:
            action = np.argmax(q_table[state])
            next_state, reward, done = env.step(action)

            q_table[state, action] += 0.1 * (
                reward + 0.9 * np.max(q_table[next_state]) - q_table[state, action]
            )

            state = next_state

    return q_table
