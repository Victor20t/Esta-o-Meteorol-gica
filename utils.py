def validar_int(numero_inteiro):
    while True:
        if str(numero_inteiro).strip() == "":
            print("Entrada vazia. Digite um número inteiro.")
            numero_inteiro = input("Digite um número inteiro: ")
            continue

        try:
            return int(numero_inteiro)
        except ValueError:
            print("Apenas digite inteiros.")
            numero_inteiro = input("Digite um número inteiro: ")


def validar_float(numero_float):
    while True:
        if str(numero_float).strip() == "":
            print("Entrada vazia. Digite um número.")
            numero_float = input("Digite um número: ")
            continue

        try:
            return float(numero_float)
        except ValueError:
            print("Apenas números.")
            numero_float = input("Digite um número: ")


def validar_umidade(umidade):
    umidade = validar_int(umidade)

    while umidade < 0 or umidade > 100:
        print("Digite a umidade entre 0 e 100.")
        umidade = validar_int(input("Digite a umidade (%): "))

    return umidade


def validar_horario(horas, minutos):
    horas = validar_int(horas)
    minutos = validar_int(minutos)

    while horas < 0 or horas > 23:
        print("Digite as horas entre 0 e 23.")
        horas = validar_int(input("Digite as horas: "))

    while minutos < 0 or minutos > 59:
        print("Digite os minutos entre 0 e 59.")
        minutos = validar_int(input("Digite os minutos: "))

    return f"{horas:02d}:{minutos:02d}"


def validar_temperatura(temperatura):
    temperatura = validar_float(temperatura)

    while temperatura < -50 or temperatura > 60:
        print("Digite uma temperatura entre -50°C e 60°C.")
        temperatura = validar_float(input("Digite a temperatura (°C): "))

    return temperatura


def validar_vento(vento):
    vento = validar_float(vento)

    while vento < 0:
        print("A velocidade do vento não pode ser negativa.")
        vento = validar_float(input("Digite a velocidade do vento (km/h): "))

    return vento


def validar_chuva(chuva):
    chuva = validar_float(chuva)

    while chuva < 0:
        print("A quantidade de chuva não pode ser negativa.")
        chuva = validar_float(input("Digite a quantidade de chuva (mm): "))

    return chuva