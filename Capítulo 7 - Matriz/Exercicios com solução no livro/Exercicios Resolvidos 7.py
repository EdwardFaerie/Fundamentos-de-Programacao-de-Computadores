# Um elemento Aij de uma matriz é dito ponto de sela da matriz A se, e somente se, Aij for, ao mesmo tempo, o menor elemento da linha i e o maior elemento da coluna j. Faça um programa que carregue uma matriz de ordem 5 x 7, verifique se a matriz possui ponto de sela e, se possuir, mostre seu valor e sua localização.

# Importar a biblioteca random para gerar números inteiros aleatórios
import random

# Criar uma matriz de ordem 5x7 com números inteiros aleatórios
matriz = [[random.randint(0, 100) for _ in range(7)] for _ in range(5)]

# Mostrar a matriz
print("Matriz:")
for linha in matriz:
    print(linha)

# Verificar se a matriz possui ponto de sela
ponto_sela = None
for i, linha in enumerate(matriz):
    menor_elemento_linha = min(linha)
    for j, elemento in enumerate(linha):
        if elemento == menor_elemento_linha:
            maior_elemento_coluna = max([linha[k][j] for k in range(5)])
            if elemento == maior_elemento_coluna:
                ponto_sela = (i, j, elemento)
                break
    if ponto_sela:
        break

# Mostrar o resultado
if ponto_sela:
    print(f"Ponto de sela encontrado: {ponto_sela[2]} na linha {ponto_sela[0]+1} e coluna {ponto_sela[1]+1}")
else:
    print("Matriz não possui ponto de sela")