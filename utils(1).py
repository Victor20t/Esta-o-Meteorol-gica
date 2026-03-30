def validar_int(numero_inteiro):
    validacao_int = None
    while validacao_int is None:
        try:
            numero_inteiro = int(numero_inteiro)
            validacao_int = True
        except ValueError:
            print('Apenas digite inteiros')
            numero_inteiro = input('Digite um número inteiro: ')
    return numero_inteiro
def validar_float(numero_float):
    validacao_float = None
    while validacao_float is None:
        try:
            numero_float= float(numero_float)
            validacao_float = True
        except ValueError:
            print('Apenas números')
            numero_float = input('Digite um número: ')
    return numero_float

def validar_horario(horas,minutos):
    validacao_horas = None
    validacao_minutos = None
    horas = validar_int(horas)
    minutos = validar_int(minutos)
    while validacao_horas is None:
        if horas > 23 or horas < 0:
            print('Digite as horas entre 0 até 23')
            horas = validar_int(input('Digite as horas: '))
        else:
          validacao_horas = True
    while validacao_minutos is None:
        if minutos > 59 or minutos < 0:
            print('Digite os minutos entre 0 até 59')
            minutos = validar_int(input('Digite os minutos: '))
        else:
          validacao_minutos = True
    horario = f"{horas:02d}:{minutos:02d}"
    return horario

def validar_temperatura(temperatura):
    validacao_temperatura = None
    temperatura = validar_int(temperatura)
    while validacao_temperatura is None:
        if temperatura < 0 or temperatura > 100:
            temperatura = validar_int(input('Digite uma temperatura maior do que 0 e menor do que 100: '))
        else:
            validacao_temperatura = True
    return temperatura



