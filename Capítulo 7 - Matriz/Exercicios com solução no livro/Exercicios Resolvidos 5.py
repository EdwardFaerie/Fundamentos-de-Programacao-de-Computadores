# Na teoria dos sistemas, define-se o elemento MINMAX de uma matriz como o maior elemento da linha em que se encontra o menor elemento da matriz. Elabore um programa que carregue uma matriz 4 x 7 com números reais, calcule e mostre seu MINMAX e sua posição (linha e coluna).

# Importar a biblioteca random para gerar números reais aleatórios
import random

# Criar uma matriz 4x7 com números reais aleatórios
matriz = [[random.uniform(0, 100) for _ in range(7)] for _ in range(4)]

# Encontrar o menor elemento da matriz e sua posição
menor_elemento = min(min(linha) for linha in matriz)
menor_linha, menor_coluna = None, None
for i, linha in enumerate(matriz):
    for j, elemento in enumerate(linha):
        if elemento == menor_elemento:
            menor_linha, menor_coluna = i, j
            break

# Encontrar o maior elemento da linha do menor elemento
max_elemento_linha = max(matriz[menor_linha])

# Mostrar o resultado
print("Matriz:")
for linha in matriz:
    print(linha)
print(f"MINMAX: {max_elemento_linha} na linha {menor_linha+1} e coluna {menor_coluna+1}")