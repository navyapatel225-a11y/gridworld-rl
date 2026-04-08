class GridEnv:
    def __init__(self):
        self.goal = 4
        self.state = 0

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        try:
            if action == 1:
                self.state = min(self.state + 1, self.goal)
            else:
                self.state = max(self.state - 1, 0)

            reward = 1 if self.state == self.goal else 0
            done = self.state == self.goal

            return self.state, reward, done

        except Exception:
            # fallback safe response
            return 0, 0, True
