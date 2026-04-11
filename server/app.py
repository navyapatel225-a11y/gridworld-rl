from fastapi import FastAPI

app = FastAPI()

# Dummy state
state_data = {"position": [0, 0]}

@app.get("/")
def root():
    return {"message": "GridWorld RL API running"}

@app.post("/reset")
def reset():
    state_data["position"] = [0, 0]
    return {"state": state_data}

@app.post("/step")
def step(action: str):
    x, y = state_data["position"]

    if action == "up":
        y += 1
    elif action == "down":
        y -= 1
    elif action == "left":
        x -= 1
    elif action == "right":
        x += 1

    state_data["position"] = [x, y]

    reward = 1.0 if [x, y] == [2, 2] else 0.0
    done = [x, y] == [2, 2]

    return {
        "state": state_data,
        "reward": reward,
        "done": done
    }

@app.get("/state")
def state():
    return state_data
