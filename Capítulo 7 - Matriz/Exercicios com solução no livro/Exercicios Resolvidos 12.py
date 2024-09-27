# Elabore um programa que preencha uma matriz 4 x 4 com números inteiros e verifique se essa matriz forma o chamado quadrado mágico. Um quadrado mágico é formado quando a soma dos elementos de cada linha é igual à soma dos elementos de cada coluna dessa linha, é igual à soma dos elementos da diagonal principal e, também, é igual à soma dos elementos da diagonal secundária

# Importar a biblioteca random para gerar números aleatórios
import random

# Criar uma matriz 4x4 com números inteiros aleatórios
matriz = [[random.randint(0, 100) for _ in range(4)] for _ in range(4)]

# Mostrar a matriz
print("Matriz:")
for linha in matriz:
    print(linha)

# Definir funções para calcular a soma de cada linha, coluna, diagonal principal e diagonal secundária
def soma_linha(matriz, i):
    # Retorna a soma dos elementos da linha i
    return sum(matriz[i])

def soma_coluna(matriz, j):
    # Retorna a soma dos elementos da coluna j
    return sum([linha[j] for linha in matriz])

def soma_diagonal_principal(matriz):
    # Retorna a soma dos elementos da diagonal principal
    return sum([matriz[i][i] for i in range(4)])

def soma_diagonal_secundaria(matriz):
    # Retorna a soma dos elementos da diagonal secundária
    return sum([matriz[i][3-i] for i in range(4)])

# Verificar se a matriz é um quadrado mágico
soma = soma_linha(matriz, 0)  # Calcular a soma da primeira linha
eh_quadrado_magico = True  # Inicializar a variável que indica se a matriz é um quadrado mágico

# Verificar se a soma de cada linha, coluna, diagonal principal e diagonal secundária é igual à soma da primeira linha
for i in range(4):
    if soma_linha(matriz, i) != soma:  # Verificar se a soma da linha i é igual à soma da primeira linha
        eh_quadrado_magico = False  # Se não for igual, a matriz não é um quadrado mágico
        break
    if soma_coluna(matriz, i) != soma:  # Verificar se a soma da coluna i é igual à soma da primeira linha
        eh_quadrado_magico = False  # Se não for igual, a matriz não é um quadrado mágico
        break
if soma_diagonal_principal(matriz) != soma:  # Verificar se a soma da diagonal principal é igual à soma da primeira linha
    eh_quadrado_magico = False  # Se não for igual, a matriz não é um quadrado mágico
if soma_diagonal_secundaria(matriz) != soma:  # Verificar se a soma da diagonal secundária é igual à soma da primeira linha
    eh_quadrado_magico = False  # Se não for igual, a matriz não é um quadrado mágico

# Mostrar o resultado
if eh_quadrado_magico:
    print("A matriz é um quadrado mágico.")  # Se a matriz for um quadrado mágico, mostrar uma mensagem
else:
    print("A matriz não é um quadrado mágico.")  # Se a matriz não for um quadrado mágico, mostrar uma mensagem