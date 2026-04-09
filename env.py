class GridEnv:
    def __init__(self):
        self.state = 0
        self.goal = 4

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        if action == 1:
            self.state += 1
        else:
            self.state -= 1

        self.state = max(0, min(4, self.state))

        reward = 1.0 if self.state == self.goal else 0.0
        done = self.state == self.goal

        return self.state, reward, done
