class GridEnv:
    def __init__(self):
        self.state = 0
        self.goal = 4

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        # action: 0 = left, 1 = right
        if action == 1:
            self.state = min(self.state + 1, self.goal)
        else:
            self.state = max(self.state - 1, 0)

        reward = 1 if self.state == self.goal else 0
        done = self.state == self.goal

        return self.state, reward, done
