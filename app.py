from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Python is working!"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from Vercel!"}
