import numpy as np
from train import train
from env import GridEnv

# Train model
q_table = train()

print("Training complete ✅")
print("Q-table:\n", q_table)

# Test policy
env = GridEnv()
state = env.reset()

path = [state]
done = False

while not done:
    action = int(np.argmax(q_table[state]))
    state, _, done = env.step(action)
    path.append(state)

print("Learned path:", path)
