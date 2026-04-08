import numpy as np
from train import train_q_learning
from env import GridEnv

# Train model once
q_table = train_q_learning()

env = GridEnv()

# Required OpenEnv-style functions

def reset():
    state = env.reset()
    return {"state": state}


def step(action):
    state, reward, done = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }


def act(state):
    state = int(state)
    action = int(np.argmax(q_table[state]))
    return action


# Optional: quick test run
if __name__ == "__main__":
    print("Testing agent...")

    state = env.reset()
    for _ in range(10):
        action = act(state)
        state, reward, done = env.step(action)
        print(state, reward, done)
        if done:
            break
