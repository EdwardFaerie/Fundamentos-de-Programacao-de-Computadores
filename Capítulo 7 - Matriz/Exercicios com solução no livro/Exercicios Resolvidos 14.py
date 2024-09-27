# Faça um programa que receba: ■ um vetor com o nome de cinco cidades diferentes; ■ uma matriz 5 x 5 com a distância entre as cidades, e na diagonal principal deve ser colocada automaticamente a distância zero, ou seja, não deve ser permitida a digitação; ■ o consumo de combustível de um veículo, ou seja, quantos quilômetros esse veículo percorre com um litro de combustível. O programa deverá calcular e mostrar: ■ os percursos que não ultrapassam 250 quilômetros (os percursos são compostos pelos nomes das cidades de origem e pelos nomes das cidades de destino); ■ todos os percursos (nome da cidade de origem e nome da cidade de destino), junto com a quantidade de combustível necessária para o veículo percorrê-los.

# Receber o vetor com o nome de cinco cidades diferentes
cidades = input("Digite os nomes de cinco cidades diferentes, separados por vírgula: ")
cidades = cidades.split(",")

# Verificar se existem realmente 5 valores de cidades
if len(cidades) != 5:
    print("Erro: você deve digitar 5 cidades diferentes.")
    exit()

# Receber a matriz 5 x 5 com a distância entre as cidades
distancias = []
for i in range(5):
    linha = []
    for j in range(5):
        if i == j:
            linha.append(0)  # Distância zero na diagonal principal
        else:
            distancia = float(input(f"Digite a distância entre {cidades[i]} e {cidades[j]}: "))
            linha.append(distancia)
    distancias.append(linha)

# Receber o consumo de combustível de um veículo
consumo_combustivel = float(input("Digite o consumo de combustível do veículo (quilômetros por litro): "))

# Calcular e mostrar os percursos que não ultrapassam 250 quilômetros
print("Percursos que não ultrapassam 250 quilômetros:")
for i in range(5):
    for j in range(5):
        if distancias[i][j] <= 250:
            print(f"{cidades[i]} -> {cidades[j]}")

# Calcular e mostrar todos os percursos com a quantidade de combustível necessária
print("\nPercursos com a quantidade de combustível necessária:")
for i in range(5):
    for j in range(5):
        combustivel_necessario = distancias[i][j] / consumo_combustivel
        print(f"{cidades[i]} -> {cidades[j]}: {combustivel_necessario:.2f} litros")