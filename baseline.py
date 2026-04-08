import asyncio
import os
from my_env_v4 import MyEnvV4Action, MyEnvV4Env

IMAGE_NAME = os.getenv("IMAGE_NAME")


async def run():
    env = await MyEnvV4Env.from_docker_image(IMAGE_NAME)
    result = await env.reset()

    for _ in range(8):
        if result.done:
            break

        result = await env.step(MyEnvV4Action(message="hello"))

        print("[BASELINE STEP]")

        if result.done:
            break

    await env.close()


if __name__ == "__main__":
    asyncio.run(run())