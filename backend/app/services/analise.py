import math
from datetime import datetime

# DETECÇÃO DE ATRASO — COMPARAÇÃO DE TEMPO ENTRE EVENTOS
def detectar_atraso(eventos):
    if len(eventos) < 2:
        return None

    ultimo = eventos[-1]
    anterior = eventos[-2]

    tempo = (ultimo.timestamp - anterior.timestamp).total_seconds()

    if tempo > 600:  # 10 minutos
        return "atraso"

    return None

def distancia(p1, p2):
    return math.sqrt(
        (p1.latitude - p2.latitude)**2 +
        (p1.longitude - p2.longitude)**2
    )

# DESVIO DE ROTA — COMPARAÇÃO COM PONTO ESPERADO
def detectar_desvio(eventos, rota_esperada):
    ultimo = eventos[-1]

    ponto_esperado = rota_esperada[-1]

    if distancia(ultimo, ponto_esperado) > 0.05:
        return "desvio_rota"

    return None

# ETA — ESTIMATIVA DE TEMPO DE CHEGADA
def calcular_eta(eventos, destino):
    if len(eventos) < 2:
        return None

    p1 = eventos[-2]
    p2 = eventos[-1]

    tempo = (p2.timestamp - p1.timestamp).total_seconds()

    dist = distancia(p1, p2)

    if tempo == 0:
        return None

    velocidade = dist / tempo

    dist_restante = distancia(p2, destino)

    if velocidade == 0:
        return None

    eta_segundos = dist_restante / velocidade

    return eta_segundos