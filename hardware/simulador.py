import requests
import random
import time

#Criar fila local
fila = []

while True:
    lat = random.uniform(-3, -4)
    lon = random.uniform(-60, -61)
    posicao = {"lat": lat, "lon": lon} #Posição atual

    try:
        #Modificar lógica
        requests.post(
            "http://localhost:8000/evento",
            params=posicao,
            timeout=3 #Importante para não travar o código se o servidor cair
        )
        print("enviado")

        # Reenvio
        # Se enviou o atual com sucesso e existem itens na fila, envia o que ficou pendente
        if fila:
            print(f"Reenviando {len(fila)} itens da fila...")
            for item in fila:
                requests.post("http://localhost:8000/evento", params=item)
            fila.clear()

    except:
        fila.append(posicao)
        print("salvo offline")

    time.sleep(2)