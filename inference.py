import numpy as np
from train import train_q_learning
from env import GridEnv

# initialize once
q_table = train_q_learning()
env = GridEnv()

# OpenEnv API

def reset():
    state = env.reset()
    return {"state": state}


def step(action):
    state, reward, done = env.step(int(action))
    return {
        "state": state,
        "reward": reward,
        "done": done
    }


def act(state):
    state = int(state)
    return int(np.argmax(q_table[state]))


# optional local debug
if __name__ == "__main__":
    s = env.reset()
    for _ in range(10):
        a = act(s)
        s, r, d = env.step(a)
        print(s, r, d)
        if d:
            break
