class GridEnv:
    def __init__(self):
        self.state = 0
        self.goal_state = 4

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        # Action: 0 = left, 1 = right
        if action == 1:
            self.state += 1
        else:
            self.state -= 1

        self.state = max(0, min(self.state, self.goal_state))

        reward = 1 if self.state == self.goal_state else 0
        done = self.state == self.goal_state

        return self.state, reward, done
