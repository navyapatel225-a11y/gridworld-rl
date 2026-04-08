import numpy as np
from train import train_q_learning
from env import GridEnv

# Initialize
q_table = train_q_learning()
env = GridEnv()

# Required OpenEnv functions

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


# Optional local test
if __name__ == "__main__":
    s = env.reset()

    for _ in range(10):
        a = act(s)
        s, r, d = env.step(a)
        print(s, r, d)

        if d:
            break
