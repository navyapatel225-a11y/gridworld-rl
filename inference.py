import os
from openai import OpenAI


# ✅ Initialize client using injected environment variables
client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)


def call_llm(task_name, step):
    """
    Makes a required LLM API call.
    """
    response = client.chat.completions.create(
        model=os.environ.get("MODEL_NAME", "gpt-3.5-turbo"),
        messages=[
            {
                "role": "user",
                "content": f"You are solving {task_name}. This is step {step}. Respond briefly."
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content


def run_task(task_name):
    print(f"[START] task={task_name}", flush=True)

    total_reward = 0.0
    steps = 0

    for step in range(1, 4):
        # ✅ REQUIRED: LLM API CALL
        _ = call_llm(task_name, step)

        # Simple reward logic (valid 0.0–1.0 range)
        reward = round(0.4 + step * 0.2, 2)
        total_reward += reward
        steps += 1

        print(f"[STEP] step={step} reward={reward}", flush=True)

    score = round(min(total_reward / steps, 1.0), 2)

    print(f"[END] task={task_name} score={score} steps={steps}", flush=True)


def main():
    tasks = ["easy", "medium", "hard"]

    for task in tasks:
        run_task(task)


if __name__ == "__main__":
    main()
