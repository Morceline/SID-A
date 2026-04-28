from app.database.connection import SessionLocal
from app.models.evento import Evento
from app.services.analise import detectar_atraso, detectar_desvio

def salvar_evento(data):
    db = SessionLocal()
    try:
        # 1. Criar o objeto conforme seu modelo
        evento = Evento(
            viagem_id=data["viagem_id"],
            latitude=data["lat"],
            longitude=data["lon"],
            tipo=data.get("tipo", "posicao")
        )

        db.add(evento)
        db.commit()
        db.refresh(evento)

        # Buscar histórico para análise 
        eventos_da_viagem = db.query(Evento).filter(Evento.viagem_id == evento.viagem_id).all()

        # Implementação solicitada
        alertas = processar_evento(eventos_da_viagem)

        return {
            "evento": evento,
            "alertas": alertas
        }
    finally:
        db.close()

def processar_evento(eventos):
    alerta = []

    atraso = detectar_atraso(eventos)
    if atraso:
        alerta.append(atraso)

    # Nota: rota_esperada vazia 
    desvio = detectar_desvio(eventos, rota_esperada=[])
    if desvio:
        alerta.append(desvio)

    return alerta