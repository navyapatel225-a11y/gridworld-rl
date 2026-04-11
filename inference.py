import time
import random

def run_task(task_name):
    print(f"[START] task={task_name}", flush=True)

    total_reward = 0.0
    steps = 0

    # simulate steps (replace this with your env logic if needed)
    for step in range(1, 4):
        reward = round(random.uniform(0.3, 1.0), 2)
        total_reward += reward
        steps += 1

        print(f"[STEP] step={step} reward={reward}", flush=True)
        time.sleep(0.2)

    # final score (normalized 0–1)
    score = round(min(total_reward / steps, 1.0), 2)

    print(f"[END] task={task_name} score={score} steps={steps}", flush=True)


def main():
    tasks = ["easy", "medium", "hard"]

    for task in tasks:
        run_task(task)


if __name__ == "__main__":
    main()
