import os
import numpy as np
from openai import OpenAI
from train import train_q_learning
from env import GridEnv

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

q_table = train_q_learning()
env = GridEnv()

def run_episode(task="gridworld"):
    state = env.reset()
    done = False
    step_count = 0
    rewards = []

    print(f"[START] task={task} env=gridworld model={MODEL_NAME}", flush=True)

    try:
        while not done and step_count < 10:
            action = int(np.argmax(q_table[state]))
            next_state, reward, done = env.step(action)

            rewards.append(f"{reward:.2f}")
            step_count += 1

            print(
                f"[STEP] step={step_count} action={action} reward={reward:.2f} done={str(done).lower()} error=null",
                flush=True
            )

            state = next_state

        success = str(done).lower()

    except Exception as e:
        success = "false"
        print(
            f"[STEP] step={step_count} action=null reward=0.00 done=true error={str(e)}",
            flush=True
        )

    finally:
        print(
            f"[END] success={success} steps={step_count} rewards={','.join(rewards)}",
            flush=True
        )

if __name__ == "__main__":
    run_episode()
