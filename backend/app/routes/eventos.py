from fastapi import APIRouter
from app.database.connection import SessionLocal
from app.models.evento import Evento
from app.services.processamento import salvar_evento

router = APIRouter()

@router.post("/evento")
def criar_evento(lat: float, lon: float, viagem_id: int = 1, tipo: str = "posicao"):
    data = {
        "lat": lat,
        "lon": lon,
        "viagem_id": viagem_id,
        "tipo": tipo
    }

    salvar_evento(data)

    return {"status": "evento salvo"}