import sys
sys.path.append("/app")

from fastapi import FastAPI
import uvicorn
import threading

from inference import run_episode

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

# 🔥 Run inference in background when server starts
def start_inference():
    run_episode()

@app.on_event("startup")
def startup_event():
    thread = threading.Thread(target=start_inference)
    thread.start()

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
