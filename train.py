import numpy as np

def train_q_learning():
    num_states = 5
    num_actions = 2

    q_table = np.zeros((num_states, num_actions))

    # Simple dummy training loop
    for episode in range(1000):
        state = np.random.randint(0, num_states)
        action = np.random.randint(0, num_actions)
        reward = np.random.random()

        # Q-learning update (simplified)
        q_table[state][action] = q_table[state][action] + 0.1 * (
            reward - q_table[state][action]
        )

    print("Training complete ✅")
    print("Q-table:\n", q_table)

    return q_table
