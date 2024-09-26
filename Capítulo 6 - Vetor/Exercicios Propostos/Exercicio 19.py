# Faça um programa que leia dois vetores de dez posições e faça a multiplicação dos elementos de mesmo índice, colocando o resultado em um terceiro vetor. Mostre o vetor resultante.

# Inicializamos três vetores vazios para armazenar os elementos
vetor1 = []
vetor2 = []
vetor3 = []

# Preenchemos o vetor 1 com 10 elementos
print("Preencha o vetor 1:")
for i in range(10):
    # Pedimos o elemento ao usuário
    elemento = int(input("Digite o {}º elemento: ".format(i+1)))
    
    # Adicionamos o elemento ao vetor 1
    vetor1.append(elemento)

# Preenchemos o vetor 2 com 10 elementos
print("\nPreencha o vetor 2:")
for i in range(10):
    # Pedimos o elemento ao usuário
    elemento = int(input("Digite o {}º elemento: ".format(i+1)))
    
    # Adicionamos o elemento ao vetor 2
    vetor2.append(elemento)

# Criamos o vetor 3 multiplicando os elementos correspondentes dos vetores 1 e 2
for i in range(10):
    vetor3.append(vetor1[i] * vetor2[i])

# Imprimimos o vetor resultante
print("\nVetor resultante:")
for elemento in vetor3:
    print(elemento)