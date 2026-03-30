def calcular_temperatura_media(medicoes):
    if len(medicoes) == 0:
        return None

    soma_temp = sum(medicao["temperatura"] for medicao in medicoes)
    return soma_temp / len(medicoes)


def calcular_temperatura_maxima(medicoes):
    if len(medicoes) == 0:
        return None

    temperaturas = [medicao["temperatura"] for medicao in medicoes]
    return max(temperaturas)


def calcular_temperatura_minima(medicoes):
    if len(medicoes) == 0:
        return None

    temperaturas = [medicao["temperatura"] for medicao in medicoes]
    return min(temperaturas)


def calcular_media_umidade(medicoes):
    if len(medicoes) == 0:
        return None

    soma_umidade = sum(medicao["umidade"] for medicao in medicoes)
    return soma_umidade / len(medicoes)


def calcular_vento_maximo(medicoes):
    if len(medicoes) == 0:
        return None

    ventos = [medicao['vento'] for medicao in medicoes]
    return max(ventos)


def calcular_quantidade_total_chuva(medicoes):
    if len(medicoes) == 0:
        return 0

    return sum(medicao["chuva"] for medicao in medicoes)


def verificar_alertas(medicao):
    alertas = []

    if medicao['temperatura'] > 35:
        alertas.append("ALERTA: Calor extremo detectado!")

    if medicao['vento'] > 40:
        alertas.append("ALERTA: Vento forte detectado!")

    if medicao['chuva'] > 20:
        alertas.append("ALERTA: Chuva intensa detectada!")

    return alertas


def calcular_total_medicoes(medicoes):
    return len(medicoes)