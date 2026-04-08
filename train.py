import numpy as np

def train_q_learning():
    num_states = 5
    num_actions = 2

    q_table = np.zeros((num_states, num_actions))

    alpha = 0.1
    gamma = 0.9
    episodes = 2000

    for _ in range(episodes):
        state = np.random.randint(0, num_states)

        done = False
        while not done:
            action = np.random.randint(0, num_actions)

            # environment transition (must match env.py)
            if action == 1:
                next_state = min(state + 1, num_states - 1)
            else:
                next_state = max(state - 1, 0)

            reward = 1 if next_state == num_states - 1 else 0
            done = reward == 1

            # Q-learning update
            q_table[state][action] += alpha * (
                reward + gamma * np.max(q_table[next_state]) - q_table[state][action]
            )

            state = next_state

    return q_table
