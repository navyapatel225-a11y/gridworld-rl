import json
import numpy as np
from environment import GridWorld
from agent import Agent

env = GridWorld()
agent = Agent()

episodes = 100

for _ in range(episodes):
    state = env.reset()
    done = False

    while not done:
        action = agent.act(state)
        next_state, reward, done = env.step(action)

        x,y = state
        nx,ny = next_state

        agent.q_table[x,y,action] += 0.1 * (
            reward + 0.9 * np.max(agent.q_table[nx,ny]) - agent.q_table[x,y,action]
        )

        state = next_state

# save
with open("q_table.json", "w") as f:
    json.dump(agent.q_table.tolist(), f)
