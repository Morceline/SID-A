from app.database.connection import SessionLocal
from app.models.evento import Evento

def salvar_evento(data):
    db = SessionLocal()

    evento = Evento(
        viagem_id=data["viagem_id"],
        latitude=data["lat"],
        longitude=data["lon"],
        tipo=data.get("tipo", "posicao")
    )

    db.add(evento)
    db.commit()

    return evento