
import dados
import utils
import services

def registrar_medicao():
    print("\n--- Registrar Nova Medição ---")
    horas = input("Digite as horas: ")
    minutos = input("Digite os minutos: ")
    horario = utils.validar_horario(horas, minutos)

    temperatura = utils.validar_temperatura(input("Digite a temperatura (°C): "))
    umidade = utils.validar_float(input("Digite a umidade (%): "))
    vento = utils.validar_float(input("Digite a velocidade do vento (km/h): "))
    chuva = utils.validar_float(input("Digite a quantidade de chuva (mm): "))

    nova_medicao = {
        'horario': horario,
        'temperatura': temperatura,
        'umidade': umidade,
        'vento': vento,
        'chuva': chuva
    }

    dados.medicoes.append(nova_medicao)
    print("Medição registrada com sucesso!")


    alertas = services.verificar_alertas(nova_medicao)
    for alerta in alertas:
        print(f"{alerta}")


def listar_medicoes():
    print("\n--- Histórico de Medições ---")
    if len(dados.medicoes) == 0:
        print("Nenhuma medição registrada ainda.")
        return

    for m in dados.medicoes:
        print(
            f"Horário: {m['horario']} | Temp: {m['temperatura']}°C | Umidade: {m['umidade']}% | Vento: {m['vento']}km/h | Chuva: {m['chuva']}mm")


def mostrar_estatisticas():
    print("\n--- Estatísticas Climáticas ---")
    if len(dados.medicoes) == 0:
        print("Sem dados para gerar estatísticas.")
        return

    print(f"Temperatura Máxima: {services.calcular_temperatura_maxima(dados.medicoes)}°C")
    print(f"Temperatura Mínima: {services.calcular_temperatura_minima(dados.medicoes)}°C")
    print(f"Temperatura Média: {services.calcular_temperatura_media(dados.medicoes):.1f}°C")
    print(f"Média da Umidade: {services.calcular_media_umidade(dados.medicoes):.1f}%")
    print(f"Vento Máximo: {services.calcular_vento_maximo(dados.medicoes)} km/h")
    print(f"Total de Chuva: {services.calcular_quantidade_total_chuva(dados.medicoes)} mm")


def gerar_relatorio():
    print("\n--- Relatório Final ---")
    print(f"Total de medições realizadas: {services.calcular_total_medicoes(dados.medicoes)}")
    mostrar_estatisticas()


def mostrar_menu():
    print("\n=== ESTAÇÃO METEOROLÓGICA ===")
    print("1 - Registrar medição")
    print("2 - Listar medições")
    print("3 - Ver estatísticas")
    print("4 - Gerar relatório final")
    print("0 - Sair")


def ler_opcao():
    return input("Escolha uma opção: ")


def executar_opcao(opcao):
    if opcao == "1":
        registrar_medicao()
    elif opcao == "2":
        listar_medicoes()
    elif opcao == "3":
        mostrar_estatisticas()
    elif opcao == "4":
        gerar_relatorio()
    elif opcao == "0":
        print("Encerrando o sistema...")
        return False
    else:
        print("Opção inválida!")
    return True


def main():
    rodando = True
    while rodando:
        mostrar_menu()
        opcao = ler_opcao()
        rodando = executar_opcao(opcao)


if __name__ == "__main__":
    main()