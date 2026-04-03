from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "SID-A backend ativo (FastAPI)"}