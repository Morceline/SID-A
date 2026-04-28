import requests
import random
import time

TOKEN = "TOKEN_DO_LOGIN"

# Criar viagem real e obter ID dinâmico
try:
    # O simulador avisa o backend que uma nova viagem começou
    response = requests.post(
        "http://localhost:8000/viagem", 
        params={"nome": "Nova Viagem Amazonia"},
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    viagem_id = response.json().get("id")
    print(f"🚢 Viagem iniciada com ID: {viagem_id}")
except:
    # Caso o backend esteja offline no início, ID padrão
    viagem_id = 1
    print("Backend offline. Usando ID padrão: 1")

# Criar fila local
fila = []

# Tipos de eventos
tipos = ["inicio", "posicao", "posicao", "posicao", "parada", "posicao", "entrega"]

while True:
    lat = random.uniform(-3, -4)
    lon = random.uniform(-60, -61)
    tipo = random.choice(tipos)

    # Variável viagem_id 
    posicao = {
        "lat": lat,
        "lon": lon,
        "tipo": tipo,
        "viagem_id": viagem_id
    }

    try:
        # Modificar lógica
        requests.post(
            "http://localhost:8000/evento",
            params=posicao,
            headers={"Authorization": f"Bearer {TOKEN}"},
            timeout=3 
        )
        print(f"enviado: {tipo} (Viagem: {viagem_id})")

        # Reenvio
        if fila:
            print(f"Reenviando {len(fila)} itens da fila...")
            for item in fila:
                requests.post(
                    "http://localhost:8000/evento", 
                    params=item,
                    headers={"Authorization": f"Bearer {TOKEN}"}
                )
            fila.clear()

    except:
        fila.append(posicao)
        print(f"salvo offline ({tipo})")

    time.sleep(2)