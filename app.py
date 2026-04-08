import gradio as gr
import numpy as np
import random

# Environment
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


# Training
def train_q_learning():
    num_states = 5
    num_actions = 2

    q_table = np.zeros((num_states, num_actions))

    alpha = 0.1
    gamma = 0.9
    epsilon = 0.2
    episodes = 500

    env = GridEnv()

    for _ in range(episodes):
        state = env.reset()
        done = False

        while not done:
            if random.uniform(0, 1) < epsilon:
                action = random.randint(0, num_actions - 1)
            else:
                action = int(np.argmax(q_table[state]))

            next_state, reward, done = env.step(action)

            q_table[state, action] += alpha * (
                reward + gamma * np.max(q_table[next_state]) - q_table[state, action]
            )

            state = next_state

    return q_table


# UI function
def run_agent():
    q_table = train_q_learning()

    env = GridEnv()
    state = env.reset()

    path = [state]
    done = False

    while not done:
        action = int(np.argmax(q_table[state]))
        state, _, done = env.step(action)
        path.append(state)

    return str(q_table), str(path)


# Gradio UI
demo = gr.Interface(
    fn=run_agent,
    inputs=[],
    outputs=["text", "text"],
    title="Gridworld RL",
    description="Train Q-learning and show results"
)

demo.launch(server_name="0.0.0.0", server_port=7860)
