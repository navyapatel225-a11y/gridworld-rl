import sys
import os
sys.path.append("/app")

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from inference import reset, step, act

app = FastAPI()

# Request models (VERY IMPORTANT)
class StepRequest(BaseModel):
    action: int

class ActRequest(BaseModel):
    state: int

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
def reset_env():
    return reset()

@app.post("/step")
def step_env(req: StepRequest):
    return step(req.action)

@app.post("/act")
def act_env(req: ActRequest):
    return {"action": act(req.state)}

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
