import sys
import os

# Fix import path
sys.path.append("/app")

from fastapi import FastAPI
import uvicorn

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

# ✅ REQUIRED main()
def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

# ✅ REQUIRED entry trigger
if __name__ == "__main__":
    main()
