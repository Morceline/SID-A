from fastapi import APIRouter, Depends
from app.database.connection import SessionLocal
from app.models.evento import Evento, Viagem
from app.services.processamento import salvar_evento
from app.services.processamento import detectar_anomalia, calcular_eta
from app.services.deps import get_usuario_logado

router = APIRouter()

@router.post("/evento")
def criar_evento(
    lat: float,
    lon: float,
    viagem_id: int,
    tipo: str,
    usuario = Depends(get_usuario_logado)
):
    db = SessionLocal()

    evento = Evento(
        viagem_id=viagem_id,
        latitude=lat,
        longitude=lon,
        tipo=tipo
    )

    db.add(evento)
    db.commit()

    return {
        "status": "evento salvo",
        "usuario": usuario.nome
    }

@router.get("/eventos")
def listar_eventos():
    db = SessionLocal()
    eventos = db.query(Evento).all()

    return [
        {
            "id": e.id,
            "viagem_id": e.viagem_id,
            "lat": e.latitude,
            "lon": e.longitude,
            "tipo": e.tipo
        }
        for e in eventos
    ]

@router.get("/viagem/{viagem_id}/eventos")
def eventos_por_viagem(viagem_id: int):
    db = SessionLocal()
    eventos = db.query(Evento).filter(Evento.viagem_id == viagem_id).all()

    return [
        {
            "lat": e.latitude,
            "lon": e.longitude,
            "tipo": e.tipo
        }
        for e in eventos
    ]

@router.get("/viagem/{viagem_id}/analise")
def analisar_viagem(viagem_id: int):
    db = SessionLocal()
    eventos = db.query(Evento).filter(Evento.viagem_id == viagem_id).all()

    tem_anomalia = detectar_anomalia(eventos)

    return {
        "anomalia": tem_anomalia,
        "total_eventos": len(eventos)
    }

@router.get("/viagem/{viagem_id}/eta")
def eta_viagem(viagem_id: int):
    db = SessionLocal()
    eventos = db.query(Evento).filter(Evento.viagem_id == viagem_id).all()

    eta = calcular_eta(eventos)

    return {"eta_estimado_minutos": eta}

@router.post("/viagem")
def criar_viagem(nome: str):
    db = SessionLocal()

    nova = Viagem(nome=nome)

    db.add(nova)
    db.commit()

    return {"id": nova.id}