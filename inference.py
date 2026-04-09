import numpy as np
from train import train_q_learning
from env import GridEnv

q_table = train_q_learning()
env = GridEnv()

def reset():
    return {"state": int(env.reset())}

def step(action):
    state, reward, done = env.step(int(action))
    return {
        "state": int(state),
        "reward": float(reward),
        "done": bool(done)
    }

def act(state):
    return int(np.argmax(q_table[int(state)]))
