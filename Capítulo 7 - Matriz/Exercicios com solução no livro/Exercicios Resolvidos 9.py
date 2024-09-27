# Crie um programa que preencha uma matriz 15 x 5 com números inteiros, calcule e mostre quais elementos da matriz se repetem e quantas vezes cada um se repete.

# Importar a biblioteca random para gerar números inteiros aleatórios
import random

# Criar uma matriz 15x5 com números inteiros aleatórios
matriz = [[random.randint(0, 100) for _ in range(5)] for _ in range(15)]

# Mostrar a matriz
print("Matriz original:")
for linha in matriz:
    print(linha)

# Criar um dicionário para armazenar os elementos repetidos
elementos_repetidos = {}

# Iterar sobre a matriz para encontrar os elementos repetidos
for linha in matriz:
    for elemento in linha:
        if elemento in elementos_repetidos:
            elementos_repetidos[elemento] += 1
        else:
            elementos_repetidos[elemento] = 1

# Mostrar os elementos repetidos e quantas vezes cada um se repete
print("Elementos repetidos:")
for elemento, contador in elementos_repetidos.items():
    if contador > 1:
        print(f"Elemento {elemento} se repete {contador} vezes")