# Elabore um programa que preencha uma matriz 10 x 10 com números inteiros, execute as trocas especificadas a seguir e mostre a matriz resultante: ■ a linha 2 com a linha 8; ■ a coluna 4 com a coluna 10; ■ a diagonal principal com a diagonal secundária; ■ a linha 5 com a coluna 10.

# Importar a biblioteca random para gerar números inteiros aleatórios
import random

# Criar uma matriz 10x10 com números inteiros aleatórios
matriz = [[random.randint(0, 100) for _ in range(10)] for _ in range(10)]

# Mostrar a matriz original
print("Matriz original:")
for linha in matriz:
    print(linha)

# Trocar a linha 2 com a linha 8
matriz[1], matriz[7] = matriz[7], matriz[1]

# Trocar a coluna 4 com a coluna 10
for i in range(10):
    matriz[i][3], matriz[i][9] = matriz[i][9], matriz[i][3]

# Trocar a diagonal principal com a diagonal secundária
for i in range(10):
    matriz[i][i], matriz[i][9-i] = matriz[i][9-i], matriz[i][i]

# Trocar a linha 5 com a coluna 10
linha_5 = matriz[4]
coluna_10 = [linha[9] for linha in matriz]
matriz[4] = coluna_10
for i in range(10):
    matriz[i][9] = linha_5[i]

# Mostrar a matriz resultante
print("Matriz resultante:")
for linha in matriz:
    print(linha)