from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse({"message": "Space is running 🚀"})

@app.get("/run")
def run(name: str = "User"):
    return JSONResponse({"message": f"Hello {name}"})
