from fastapi import FastAPI
from app.database.connection import Base, engine
from app.models import viagem, evento
#Importando as rotas
from app.routes import eventos 

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

#Registrando as rotas de eventos no app
app.include_router(eventos.router)

@app.get("/")
def home():
    return {"mensagem": "SID-A rodando com banco"}