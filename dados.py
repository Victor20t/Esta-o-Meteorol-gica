medicoes = []

def adicionar_medicao(horario, temperatura, umidade, vento, chuva):
    medicoes.append({
        "horario": horario,
        "temperatura": temperatura,
        "umidade": umidade,
        "vento": vento,
        "chuva": chuva
    })