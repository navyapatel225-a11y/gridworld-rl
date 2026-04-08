from fastapi import FastAPI

app = FastAPI()

# initial state
state = [0, 0]

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
def reset():
    global state
    state = [0, 0]
    return {"state": state}

@app.post("/step")
def step(action: int):
    global state

    # movement: 0=up, 1=down, 2=left, 3=right
    if action == 0:
        state[0] -= 1
    elif action == 1:
        state[0] += 1
    elif action == 2:
        state[1] -= 1
    elif action == 3:
        state[1] += 1

    # keep inside grid (5x5)
    state[0] = max(0, min(state[0], 4))
    state[1] = max(0, min(state[1], 4))

    # reward logic
    if state == [4, 4]:
        reward = 1.0
        done = True
    else:
        reward = -0.1
        done = False

    return {
        "state": state,
        "reward": reward,
        "done": done
    }

# required for OpenEnv
def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
