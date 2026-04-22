def detectar_anomalia(eventos):
    if len(eventos) < 2:
        return None

    ultimo = eventos[-1]
    anterior = eventos[-2]

    # parada prolongada (simples)
    if ultimo.tipo == "posicao" and anterior.tipo == "posicao":
        return "possivel_parada"

    return None