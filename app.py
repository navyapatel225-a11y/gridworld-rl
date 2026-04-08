from fastapi import FastAPI
from fastapi.responses import JSONResponse
from task import run_task

app = FastAPI()

@app.get("/")
def health():
    return JSONResponse({"status": "ok"})

@app.get("/run")
def run(name: str = "User"):
    result = run_task(name)
    return JSONResponse({"input": name, "output": result})
