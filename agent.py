import os
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
API_KEY = os.getenv("HF_TOKEN") or os.getenv("API_KEY")

SYSTEM_PROMPT = "You are an agent that generates short meaningful messages."


class Agent:
    def __init__(self):
        self.client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

    def act(self, step, last_echo, last_reward, history):
        prompt = f"""
Step: {step}
Last echo: {last_echo}
Last reward: {last_reward}

History: {history[-3:] if history else "None"}

Reply with one short message.
"""

        try:
            res = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=150,
            )
            return res.choices[0].message.content.strip()
        except:
            return "hello"