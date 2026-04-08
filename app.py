from fastapi import FastAPI
from fastapi.responses import JSONResponse
from task import run_task

app = FastAPI()

@app.get("/")
def home():
    return JSONResponse({"status": "running"})

@app.get("/run")
def run(name: str = "User"):
    result = run_task(name)
    return JSONResponse({"result": result})
