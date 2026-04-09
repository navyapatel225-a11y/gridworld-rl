import sys
sys.path.append("/app")

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

class Dummy(BaseModel):
    x: int = 0

@app.post("/reset")
def reset():
    return {"state": 0}

@app.post("/step")
def step(d: Dummy):
    return {"state": 1, "reward": 0.0, "done": False}

@app.post("/act")
def act(d: Dummy):
    return {"action": 1}

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
