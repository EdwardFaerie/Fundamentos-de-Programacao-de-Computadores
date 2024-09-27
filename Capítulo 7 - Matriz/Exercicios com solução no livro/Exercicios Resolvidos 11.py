# Crie um programa que preencha uma matriz 8 x 8 com números inteiros e mostre uma mensagem dizendo se a matriz digitada é simétrica. Uma matriz só pode ser considerada simétrica se A[i,j] = A[j,i].

# Importar a biblioteca random para gerar números inteiros aleatórios
import random

# Criar uma matriz 8x8 com números inteiros aleatórios
matriz = [[random.randint(0, 100) for _ in range(8)] for _ in range(8)]

# Mostrar a matriz
print("Matriz:")
for linha in matriz:
    print(linha)

# Verificar se a matriz é simétrica
simetrica = True
for i in range(8):
    for j in range(8):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break
    if not simetrica:
        break

# Mostrar o resultado
if simetrica:
    print("A matriz é simétrica.")
else:
    print("A matriz não é simétrica.")