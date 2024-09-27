# Crie um programa que preencha uma primeira matriz de ordem 4 x 5 e uma segunda matriz 5 x 2. O programa deverá, também, calcular e mostrar a matriz resultante do produto matricial das duas matrizes anteriores, armazenando-o em uma terceira matriz de ordem 4 x 2.

# Importar a biblioteca random para gerar números inteiros aleatórios
import random

# Criar a primeira matriz de ordem 4x5 com números inteiros aleatórios
matriz1 = [[random.randint(0, 10) for _ in range(5)] for _ in range(4)]

# Criar a segunda matriz de ordem 5x2 com números inteiros aleatórios
matriz2 = [[random.randint(0, 10) for _ in range(2)] for _ in range(5)]

# Criar a matriz resultante de ordem 4x2
matriz_resultante = [[0 for _ in range(2)] for _ in range(4)]

# Calcular o produto matricial das duas matrizes
for i in range(4):
    for j in range(2):
        for k in range(5):
            matriz_resultante[i][j] += matriz1[i][k] * matriz2[k][j]

# Mostrar as matrizes
print("Matriz 1:")
for linha in matriz1:
    print(linha)
print("Matriz 2:")
for linha in matriz2:
    print(linha)
print("Matriz resultante:")
for linha in matriz_resultante:
    print(linha)