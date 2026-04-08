from fastapi import FastAPI
from fastapi.responses import JSONResponse
from inference import predict

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse({"status": "running"})

@app.get("/run")
def run(name: str = "User"):
    output = predict(name)
    return JSONResponse({"input": name, "output": output})
