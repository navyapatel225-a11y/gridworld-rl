import os

# Import environment (make sure this exists in your setup)
from my_env_v4 import MyEnvV4Env


class EnvWrapper:
    def __init__(self, image_name: str):
        self.image_name = image_name
        self.env = None

    async def reset(self):
        """
        Initialize and reset the environment
        """
        self.env = await MyEnvV4Env.from_docker_image(self.image_name)
        result = await self.env.reset()
        return result

    async def step(self, action):
        """
        Take a step in the environment
        """
        if self.env is None:
            raise RuntimeError("Environment not initialized. Call reset() first.")

        result = await self.env.step(action)
        return result

    async def close(self):
        """
        Close the environment safely
        """
        if self.env is not None:
            try:
                await self.env.close()
            except Exception as e:
                print(f"[WARN] Error closing env: {e}")
            self.env = None