# Faça um programa que receba a temperatura média de cada mês do ano amarzene-os em uma lista, calcule e mostre a maior e menor temperatura do ano e em que mês ocorreram (mostrar o mês por extenso desconsiderando empates)

# Ano atual
Ano = 2024

# Lista de meses do ano
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

# Lista vazia para armazenar as temperaturas médias de cada mês
temperaturas = []

# Loop para preencher a lista de temperaturas médias
for index, value in enumerate(meses):
    # Pede ao usuário que digite a temperatura média de cada mês
    temperaturas.append(float(input(f"Temperatura média de {value} em {Ano}: ")))

# Encontra a temperatura máxima e mínima
temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)

# Encontra o mês com a temperatura máxima e mínima
mes_maximo = meses[temperaturas.index(temperatura_maxima)]
mes_minimo = meses[temperaturas.index(temperatura_minima)]

# Loop para imprimir as temperaturas médias de cada mês
for index, value in enumerate(meses):
    # Imprime o mês e a temperatura média correspondente
    print(f"Mês: {value}; Temperatura: {temperaturas[index]}")

# Imprime o mês com a temperatura máxima e mínima
print(f"Mês com maior temperatura média: {mes_maximo}; com {temperatura_maxima} Graus")
print(f"Mês com menor temperatura média: {mes_minimo}; com {temperatura_minima} Graus")