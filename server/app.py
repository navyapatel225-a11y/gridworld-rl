import sys
import os
from fastapi import FastAPI
import uvicorn

# Fix import path (VERY IMPORTANT)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from inference import reset, step, act

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
def reset_env():
    return reset()

@app.post("/step")
def step_env(action: int):
    return step(action)

@app.post("/act")
def act_env(state: int):
    return {"action": act(state)}

# Keep server alive
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
