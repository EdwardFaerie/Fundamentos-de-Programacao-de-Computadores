# Elabore um programa que preencha: ■ um vetor com cinco números inteiros; ■ outro vetor com dez números inteiros; ■ uma matriz 4 x 3, também com números inteiros. O programa deverá calcular e mostrar: ■ o maior elemento do primeiro vetor multiplicado pelo menor elemento do segundo vetor. O resultado dessa multiplicação, adicionado aos elementos digitados na matriz, dará origem a uma segunda matriz (resultante); ■ a soma dos elementos pares de cada linha da matriz resultante; ■ a quantidade de elementos entre 1 e 5 em cada coluna da matriz resultante.

# Preencher o vetor com cinco números inteiros
vetor1 = []
for i in range(5):
    vetor1.append(int(input(f"Digite o {i+1}º número inteiro: ")))

# Preencher o vetor com dez números inteiros
vetor2 = []
for i in range(10):
    vetor2.append(int(input(f"Digite o {i+1}º número inteiro: ")))

# Preencher a matriz 4 x 3 com números inteiros
matriz = []
for i in range(4):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Digite o elemento [{i+1}][{j+1}] da matriz: ")))
    matriz.append(linha)

# Calcular o maior elemento do primeiro vetor multiplicado pelo menor elemento do segundo vetor
maior_vetor1 = max(vetor1)
menor_vetor2 = min(vetor2)
produto = maior_vetor1 * menor_vetor2

# Calcular a segunda matriz resultante
matriz_resultante = []
for i in range(4):
    linha = []
    for j in range(3):
        linha.append(matriz[i][j] + produto)
    matriz_resultante.append(linha)

# Mostrar a matriz resultante
print("Matriz resultante:")
for linha in matriz_resultante:
    print(linha)

# Calcular a soma dos elementos pares de cada linha da matriz resultante
soma_pares = []
for i in range(4):
    soma = 0
    for j in range(3):
        if matriz_resultante[i][j] % 2 == 0:
            soma += matriz_resultante[i][j]
    soma_pares.append(soma)

# Mostrar a soma dos elementos pares de cada linha da matriz resultante
print("Soma dos elementos pares de cada linha da matriz resultante:")
for i in range(4):
    print(f"Linha {i+1}: {soma_pares[i]}")

# Calcular a quantidade de elementos entre 1 e 5 em cada coluna da matriz resultante
quantidade_entre_1_e_5 = []
for j in range(3):
    quantidade = 0
    for i in range(4):
        if 1 <= matriz_resultante[i][j] <= 5:
            quantidade += 1
    quantidade_entre_1_e_5.append(quantidade)

# Mostrar a quantidade de elementos entre 1 e 5 em cada coluna da matriz resultante
print("Quantidade de elementos entre 1 e 5 em cada coluna da matriz resultante:")
for j in range(3):
    print(f"Coluna {j+1}: {quantidade_entre_1_e_5[j]}")