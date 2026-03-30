import dados
import utils
import service
import time

def print_delay(msg):
    print(msg)
    time.sleep(0.05)

def registrar_medicao():
    print("\n--- Registrar Nova Medição ---")
    try:
        entrada = input("Digite o horario: exemplo 14:12: ").strip()
        if entrada == "":
            print_delay("O horário não pode estar vazio.")
            return

        horas, minutos = entrada.split(":")
        horario = utils.validar_horario(horas, minutos)
    except ValueError:
        print_delay("Formato inválido. Use: HH:MM (ex: 14:30)")
        return

    temperatura = utils.validar_temperatura(input("Digite a temperatura (°C): "))
    umidade = utils.validar_umidade(input("Digite a umidade (%): "))
    vento = utils.validar_vento(input("Digite a velocidade do vento (km/h): "))
    chuva = utils.validar_chuva(input("Digite a quantidade de chuva (mm): "))

    dados.adicionar_medicao(horario, temperatura, umidade, vento, chuva)

    nova_medicao = {
        "horario": horario,
        "temperatura": temperatura,
        "umidade": umidade,
        "vento": vento,
        "chuva": chuva
    }

    print_delay("Medição registrada com sucesso!")

    alertas = service.verificar_alertas(nova_medicao)
    for alerta in alertas:
        print_delay(alerta)


def listar_medicoes():
    print_delay("\n--- Histórico de Medições ---")
    
    if not dados.medicoes:
        print_delay("Nenhuma medição registrada ainda.")
        return

    medicoes_ordenadas = sorted(dados.medicoes, key=lambda m: m['horario'])

    for m in medicoes_ordenadas:
        print_delay(
            f"Horário: {m['horario']} | Temp: {m['temperatura']}°C | "
            f"Umidade: {m['umidade']}% | Vento: {m['vento']}km/h | Chuva: {m['chuva']}mm"
        )


def mostrar_estatisticas():
    print_delay("\n--- Estatísticas Climáticas ---")
    
    if not dados.medicoes:
        print_delay("Sem dados para gerar estatísticas.")
        return

    print_delay(f"Temperatura Máxima: {service.calcular_temperatura_maxima(dados.medicoes)}°C")
    print_delay(f"Temperatura Mínima: {service.calcular_temperatura_minima(dados.medicoes)}°C")
    print_delay(f"Temperatura Média: {service.calcular_temperatura_media(dados.medicoes):.1f}°C")
    print_delay(f"Média da Umidade: {service.calcular_media_umidade(dados.medicoes):.1f}%")
    print_delay(f"Vento Máximo: {service.calcular_vento_maximo(dados.medicoes)} km/h")
    print_delay(f"Total de Chuva: {service.calcular_quantidade_total_chuva(dados.medicoes)} mm")


def gerar_relatorio():
    print_delay("\n=== RELATÓRIO FINAL DO DIA ===")

    if not dados.medicoes:
        print_delay("Nenhuma medição registrada.")
        return

    print_delay(f"Total de medições realizadas: {service.calcular_total_medicoes(dados.medicoes)}")
    print_delay(f"Temperatura Máxima: {service.calcular_temperatura_maxima(dados.medicoes)}°C")
    print_delay(f"Temperatura Mínima: {service.calcular_temperatura_minima(dados.medicoes)}°C")
    print_delay(f"Temperatura Média: {service.calcular_temperatura_media(dados.medicoes):.1f}°C")
    print_delay(f"Média da Umidade: {service.calcular_media_umidade(dados.medicoes):.1f}%")
    print_delay(f"Vento Máximo: {service.calcular_vento_maximo(dados.medicoes)} km/h")
    print_delay(f"Total de Chuva: {service.calcular_quantidade_total_chuva(dados.medicoes)} mm")

    print_delay("\nResumo do dia:")
    if service.calcular_quantidade_total_chuva(dados.medicoes) > 0:
        print_delay("- Houve registro de chuva.")
    else:
        print_delay("- Não houve chuva registrada.")

    if service.calcular_temperatura_maxima(dados.medicoes) >= 35:
        print_delay("- O dia apresentou calor intenso.")
    else:
        print_delay("- O dia não apresentou calor extremo.")

    if service.calcular_vento_maximo(dados.medicoes) >= 40:
        print_delay("- Houve ocorrência de vento forte.")
    else:
        print_delay("- Não houve vento forte.")

def mostrar_menu():
    print_delay("\n=== ESTAÇÃO METEOROLÓGICA ===")
    print_delay("1 - Registrar medição")
    print_delay("2 - Listar medições")
    print_delay("3 - Ver estatísticas")
    print_delay("4 - Gerar relatório final")
    print_delay("0 - Sair")


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
        print_delay("Encerrando o sistema...")
        return False
    else:
        print_delay("Opção inválida!")
    return True


def main():
    rodando = True
    while rodando:
        mostrar_menu()
        opcao = ler_opcao()
        rodando = executar_opcao(opcao)


if __name__ == "__main__":
    main()