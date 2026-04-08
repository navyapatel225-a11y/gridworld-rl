import numpy as np
import random

# ---------------------------
# Environment (simple grid)
# ---------------------------
# States: 0 to 4 (linear world)
# Actions: 0 = left, 1 = right

num_states = 5
num_actions = 2

# Initialize Q-table
q_table = np.zeros((num_states, num_actions))

# Hyperparameters
alpha = 0.1   # learning rate
gamma = 0.9   # discount factor
epsilon = 0.2 # exploration rate

episodes = 500

# ---------------------------
# Environment rules
# ---------------------------
def step(state, action):
    # action 0 = left, 1 = right
    if action == 0:
        next_state = max(0, state - 1)
    else:
        next_state = min(num_states - 1, state + 1)

    # reward only at final state
    reward = 1 if next_state == num_states - 1 else 0
    done = next_state == num_states - 1

    return next_state, reward, done

# ---------------------------
# Training loop
# ---------------------------
for episode in range(episodes):
    state = 0  # start state

    done = False
    while not done:
        # Exploration vs exploitation
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, num_actions - 1)
        else:
            action = np.argmax(q_table[state])

        next_state, reward, done = step(state, action)

        # Q-learning update
        q_table[state, action] = q_table[state, action] + alpha * (
            reward + gamma * np.max(q_table[next_state]) - q_table[state, action]
        )

        state = next_state

# ---------------------------
# Final Q-table
# ---------------------------
print("Trained Q-table:\n")
print(q_table)

# ---------------------------
# Test the learned policy
# ---------------------------
state = 0
path = [state]

while state != num_states - 1:
    action = np.argmax(q_table[state])
    state, _, _ = step(state, action)
    path.append(state)

print("\nBest path learned:")
print(path)
