import numpy as np
from train import train_q_learning
from env import GridEnv

class Agent:
    def __init__(self):
        self.q_table = train_q_learning()
        self.env = GridEnv()

    def reset(self):
        state = self.env.reset()
        return {"state": state}

    def step(self, action):
        state, reward, done = self.env.step(action)
        return {
            "state": state,
            "reward": reward,
            "done": done
        }

    def act(self, state):
        action = int(np.argmax(self.q_table[state]))
        return action


# Required entry point
agent = Agent()


def reset():
    return agent.reset()


def step(action):
    return agent.step(action)


def act(state):
    return agent.act(state)
