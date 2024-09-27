# Crie um programa que utilize uma matriz com dimensões máximas de cinco linhas e quatro colunas e solicite que sejam digitados os números (desordenadamente), armazenando-os, ordenadamente, na matriz.

# Inicializar a matriz com dimensões máximas de cinco linhas e quatro colunas
matriz = [[0 for _ in range(4)] for _ in range(5)]

# Inicializar a lista para armazenar os números digitados
numeros = []

# Loop para preencher a lista de números
for i in range(20):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Ordenar a lista de números
numeros.sort()

# Preencher a matriz com os números ordenados
indice = 0
for i in range(5):
    for j in range(4):
        matriz[i][j] = numeros[indice]
        indice += 1

# Mostrar a matriz
print("Matriz:")
for linha in matriz:
    print(linha)