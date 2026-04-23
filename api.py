from fastapi import FastAPI
from main import ask

app = FastAPI()

@app.get("/query")
def query(q: str):
    return {"response": ask(q)}