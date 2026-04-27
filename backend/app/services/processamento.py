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

def detectar_anomalia(eventos):
    if len(eventos) < 2:
        return False

    ultimo = eventos[-1]
    anterior = eventos[-2]

    # Regra: Duas paradas seguidas podem indicar um problema logístico ou de segurança
    if ultimo.tipo == "parada" and anterior.tipo == "parada":
        return True

    return False

def calcular_eta(eventos):
    if len(eventos) < 2:
        return None

    # Simples: quantidade de pontos restantes (simulado)
    pontos_restantes = 10 - len(eventos)

    velocidade_media = 1  # mock

    return pontos_restantes / velocidade_media