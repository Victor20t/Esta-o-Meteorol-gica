# Estação-Meteorologica

# 🌦️ Estação Meteorológica em Python

## Descrição do Projeto

Este projeto consiste no desenvolvimento de um sistema de **Estação Meteorológica em terminal**, utilizando a linguagem Python.

O sistema permite registrar medições climáticas ao longo do tempo e gerar análises estatísticas, além de emitir alertas com base em condições climáticas específicas.

O objetivo principal é aplicar conceitos fundamentais de programação, como:

- Estruturas de dados (listas e dicionários)
- Modularização do código
- Validação de entrada
- Funções e organização de código
- Lógica de programação

---

## ⚙️ Funcionalidades

O sistema possui as seguintes funcionalidades:

- Registrar medições climáticas
- Listar medições (ordenadas por horário)
- Calcular estatísticas:
  - Temperatura máxima, mínima e média
  - Média de umidade
  - Velocidade máxima do vento
  - Total de chuva
- Gerar alertas:
  - Calor extremo
  - Temperatura baixa
  - Vento forte
  - Chuva intensa
- Gerar relatório final do dia

---

## Estrutura do Projeto

O projeto está dividido em módulos para melhor organização:
📁 projeto/
│

├── main.py # Interface e menu do sistema

├── services.py # Regras de negócio e cálculos

├── utils.py # Validações de entrada

├── dados.py # Armazenamento das medições

└── README.md

---

## ## Como executar o projeto

###  Clonar o repositório

Abra o terminal (ou Git Bash) e execute:


 ```bash 
 git clone https://github.com/Victor20t/Esta-o-Meteorol-gica.git
 ```


### Pré-requisitos

- Python 3 instalado (recomendado: Python 3.10 ou superior)

---

### Como usar o sistema

Ao iniciar o programa, será exibido um menu com as opções:

1 - Registrar medição
2 - Listar medições
3 - Ver estatísticas
4 - Gerar relatório final
0 - Sair

### Registro de medição

O usuário deverá informar:

Horário (formato HH:MM)
Temperatura (float, ex: 24.5)
Umidade (0 a 100)
Velocidade do vento (valor positivo)
Quantidade de chuva (valor positivo)

Após o registro, o sistema pode exibir alertas automaticamente.

### ⚠️ Regras de validação

O sistema possui validações para garantir entradas corretas:

Horário deve estar no formato HH:MM
Horas entre 0 e 23
Minutos entre 0 e 59
Temperatura entre -50°C e 60°C
Umidade entre 0% e 100%
Vento e chuva não podem ser negativos
Não são aceitas entradas vazias

### Testes
O sistema foi validado através de um conjunto de casos de teste, incluindo:

Entradas válidas e inválidas
Valores fora dos limites
Geração de alertas
Situações sem dados cadastrados
Ordenação de medições


