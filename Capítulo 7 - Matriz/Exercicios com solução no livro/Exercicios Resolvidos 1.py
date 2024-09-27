# Faça um programa que preencha uma matriz M (2 x 2), calcule e mostre a matriz R, resultante da multiplicação dos elementos de M pelo seu maior elemento

# Preenche uma matriz 2x2 com valores fornecidos pelo usuário
M = [[float(input(f"Digite o valor da posição [1][{j+1}]: ")) for j in range(2)] for i in range(2)]

# Encontra o maior elemento na matriz M
maior_elemento = max(max(linha) for linha in M)

# Multiplica cada elemento da matriz M pelo maior elemento
R = [[elemento * maior_elemento for elemento in linha] for linha in M]

# Imprime a matriz resultante R
print("Matriz R:")
for linha in R:
    print(" ".join(f"{elemento:.2f}" for elemento in linha))