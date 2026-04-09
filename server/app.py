import sys
import os
sys.path.append("/app")

from fastapi import FastAPI, Request
import uvicorn

from inference import reset, step, act

app = FastAPI()

# ✅ health check
@app.get("/")
def root():
    return {"status": "ok"}

# ✅ RESET
@app.post("/reset")
async def reset_env():
    return reset()

# ✅ STEP (handles BOTH json + query)
@app.post("/step")
async def step_env(request: Request):
    try:
        data = await request.json()
        action = data.get("action", 0)
    except:
        action = 0
    return step(action)

# ✅ ACT (handles BOTH json + query)
@app.post("/act")
async def act_env(request: Request):
    try:
        data = await request.json()
        state = data.get("state", 0)
    except:
        state = 0
    return {"action": act(state)}

# REQUIRED
def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
