# Crie um programa que leia um vetor vet contendo 18 elementos. A seguir, o programa deverá distribuir esses elementos em uma matriz 3 x 6 e, no final, mostrar a matriz gerada.

# Ler o vetor vet contendo 18 elementos
vet = []
for i in range(18):
    vet.append(int(input(f"Digite o {i+1}º elemento do vetor: ")))

# Distribuir os elementos do vetor em uma matriz 3 × 6
matriz = []
for i in range(3):
    linha = []
    for j in range(6):
        linha.append(vet[i*6 + j])
    matriz.append(linha)

# Mostrar a matriz gerada
print("Matriz gerada:")
for linha in matriz:
    print(linha)