# Elabore um programa que preencha uma matriz 6 x 4 com números inteiros, calcule e mostre quantos elementos dessa matriz são maiores que 30 e, em seguida, monte uma segunda matriz com os elementos diferentes de 30. No lugar do número 30, da segunda matriz, coloque o número zero.

# Importar a biblioteca random para gerar números inteiros aleatórios
import random

# Criar uma matriz 6x4 com números inteiros aleatórios
matriz = [[random.randint(0, 100) for _ in range(4)] for _ in range(6)]

# Mostrar a matriz
print("Matriz original:")
for linha in matriz:
    print(linha)

# Contar quantos elementos são maiores que 30
contador = 0
for linha in matriz:
    for elemento in linha:
        if elemento > 30:
            contador += 1

print(f"Quantos elementos são maiores que 30: {contador}")

# Criar uma segunda matriz com os elementos diferentes de 30
matriz_segunda = [[0 if elemento == 30 else elemento for elemento in linha] for linha in matriz]

# Mostrar a segunda matriz
print("Matriz segunda:")
for linha in matriz_segunda:
    print(linha)