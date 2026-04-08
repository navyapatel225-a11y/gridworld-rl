from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return JSONResponse({"message": "App is running 🚀"})

@app.get("/hello")
def hello(name: str = "User"):
    return JSONResponse({"message": f"Hello {name}"})
