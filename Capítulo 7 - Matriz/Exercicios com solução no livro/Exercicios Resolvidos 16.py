# Faça um programa que preencha uma matriz 7 x 7 de números inteiros e crie dois vetores com sete posições cada um que contenham, respectivamente, o maior elemento de cada uma das linhas e o menor elemento de cada uma das colunas. Escreva a matriz e os dois vetores gerados.

# Preencher a matriz 7 x 7 de números inteiros
matriz = []  # Cria uma lista vazia para armazenar a matriz
for i in range(7):  # Loop para preencher as linhas da matriz
    linha = []  # Cria uma lista vazia para armazenar a linha atual
    for j in range(7):  # Loop para preencher as colunas da linha atual
        linha.append(int(input(f"Digite o elemento [{i+1}][{j+1}] da matriz: ")))  # Lê o elemento da matriz e o adiciona à linha
    matriz.append(linha)  # Adiciona a linha à matriz

# Criar os vetores com o maior elemento de cada linha e o menor elemento de cada coluna
maior_linha = []  # Cria uma lista vazia para armazenar o maior elemento de cada linha
menor_coluna = []  # Cria uma lista vazia para armazenar o menor elemento de cada coluna

for i in range(7):  # Loop para encontrar o maior elemento de cada linha
    maior_linha.append(max(matriz[i]))  # Encontra o maior elemento da linha atual e o adiciona ao vetor

for j in range(7):  # Loop para encontrar o menor elemento de cada coluna
    coluna = [matriz[i][j] for i in range(7)]  # Cria uma lista com os elementos da coluna atual
    menor_coluna.append(min(coluna))  # Encontra o menor elemento da coluna atual e o adiciona ao vetor

# Escrever a matriz e os dois vetores gerados
print("Matriz:")  # Imprime o título da matriz
for linha in matriz:  # Loop para imprimir as linhas da matriz
    print(linha)  # Imprime a linha atual

print("\nMaior elemento de cada linha:")  # Imprime o título do vetor de maior elemento de cada linha
print(maior_linha)  # Imprime o vetor de maior elemento de cada linha

print("\nMenor elemento de cada coluna:")  # Imprime o título do vetor de menor elemento de cada coluna
print(menor_coluna)  # Imprime o vetor de menor elemento de cada coluna