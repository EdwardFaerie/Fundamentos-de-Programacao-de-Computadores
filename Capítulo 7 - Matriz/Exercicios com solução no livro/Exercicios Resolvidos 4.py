# Crie um programa que preencha uma matriz 10 x 20 com números inteiros e some cada uma das linhas, armazenando o resultado das somas em um vetor. A seguir, o programa deverá multiplicar cada elemento da matriz pela soma da linha correspondente e mostrar a matriz resultante. 

# Importar a biblioteca random para gerar números inteiros aleatórios
import random

# Criar uma matriz 10x20 com números inteiros aleatórios
matriz = [[random.randint(0, 100) for _ in range(20)] for _ in range(10)]

# Criar um vetor para armazenar as somas das linhas
somas_linhas = [0] * 10

# Calcular a soma de cada linha e armazenar no vetor
for i, linha in enumerate(matriz):
    somas_linhas[i] = sum(linha)

# Multiplicar cada elemento da matriz pela soma da linha correspondente
for i, linha in enumerate(matriz):
    for j, elemento in enumerate(linha):
        matriz[i][j] *= somas_linhas[i]

# Mostrar a matriz resultante
print("Matriz resultante:")
for linha in matriz:
    print(linha)