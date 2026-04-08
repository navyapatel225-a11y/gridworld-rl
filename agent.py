import numpy as np

class Agent:
    def __init__(self):
        self.q_table = np.zeros((5,5,4))

    def act(self, state):
        x, y = state
        return np.argmax(self.q_table[x,y])
