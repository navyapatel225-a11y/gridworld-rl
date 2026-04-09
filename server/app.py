from fastapi import FastAPI
import uvicorn

from inference import reset, step, act

app = FastAPI()

@app.post("/reset")
def reset_env():
    return reset()

@app.post("/step")
def step_env(action: int):
    return step(action)

@app.post("/act")
def act_env(state: int):
    return {"action": act(state)}

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)
