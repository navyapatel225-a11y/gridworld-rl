import os
import numpy as np
from openai import OpenAI
from train import train_q_learning
from env import GridEnv

# 🚨 REQUIRED ENV VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
API_KEY = os.getenv("HF_TOKEN")  # using HF_TOKEN as API key

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY
)

q_table = train_q_learning()
env = GridEnv()

def run_episode(task="gridworld"):
    state = env.reset()
    done = False
    steps = 0
    total_reward = 0.0

    print(f"[START] task={task} env=gridworld model={MODEL_NAME}", flush=True)

    while not done and steps < 10:
        action = int(np.argmax(q_table[state]))
        state, reward, done = env.step(action)

        total_reward += reward
        steps += 1

        print(
            f"[STEP] step={steps} action={action} reward={reward:.2f} done={str(done).lower()} error=null",
            flush=True
        )

    score = total_reward

    # 🚨 EMAIL REQUIRED FORMAT
    print(f"[END] task={task} score={score:.2f} steps={steps}", flush=True)


if __name__ == "__main__":
    run_episode()
