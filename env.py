class GridEnv:
    def __init__(self, size=5):
        self.size = size
        self.state = 0

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        if action == 0:
            self.state = max(0, self.state - 1)
        else:
            self.state = min(self.size - 1, self.state + 1)

        reward = 1 if self.state == self.size - 1 else 0
        done = self.state == self.size - 1

        return self.state, reward, done
