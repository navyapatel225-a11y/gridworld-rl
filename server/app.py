from fastapi import FastAPI

app = FastAPI()

state = {"position": 0}

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
def reset():
    global state
    state = {"position": 0}
    return {"state": state}

@app.post("/step")
def step(action: int):
    global state
    state["position"] += int(action)

    return {
        "state": state,
        "reward": 1.0,
        "done": False
    }

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
