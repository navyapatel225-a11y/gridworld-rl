import numpy as np

class GridWorld:
    def __init__(self):
        self.size = 5
        self.reset()

    def reset(self):
        self.position = [0, 0]
        return tuple(self.position)

    def step(self, action):
        if action == 0: self.position[0] -= 1
        if action == 1: self.position[0] += 1
        if action == 2: self.position[1] -= 1
        if action == 3: self.position[1] += 1

        self.position[0] = max(0, min(self.position[0], self.size - 1))
        self.position[1] = max(0, min(self.position[1], self.size - 1))

        reward = 1 if self.position == [4,4] else -0.1
        done = self.position == [4,4]

        return tuple(self.position), reward, done
