import numpy as np

# Safe imports
try:
    from train import train_q_learning
    from env import GridEnv
except Exception as e:
    print("Import error:", e)
    train_q_learning = None
    GridEnv = None

# Initialize safely
try:
    q_table = train_q_learning() if train_q_learning else np.zeros((5, 2))
    env = GridEnv() if GridEnv else None
except Exception as e:
    print("Init error:", e)
    q_table = np.zeros((5, 2))
    env = None

# OpenEnv functions

def reset():
    try:
        if env:
            state = env.reset()
        else:
            state = 0
        return {"state": state}
    except Exception:
        return {"state": 0}


def step(action):
    try:
        if env:
            state, reward, done = env.step(int(action))
        else:
            state, reward, done = 0, 0, True

        return {"state": state, "reward": reward, "done": done}

    except Exception:
        return {"state": 0, "reward": 0, "done": True}


def act(state):
    try:
        state = int(state)
        return int(np.argmax(q_table[state]))
    except Exception:
        return 0


# Safe execution
if __name__ == "__main__":
    try:
        if env:
            s = env.reset()
            for _ in range(5):
                a = act(s)
                s, r, d = env.step(a)
                print(s, r, d)
                if d:
                    break
    except Exception as e:
        print("Runtime test error:", e)
