# Faça um programa que preencha dois vetores de dez posições cada, determine e mostre um terceiro contendo os elementos dos dois vetores anteriores ordenados de maneira decrescente

# Inicializamos dois vetores vazios para armazenar os elementos
vetor1 = []
vetor2 = []

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

# Concatenamos os vetores 1 e 2 e ordenamos o resultado em ordem decrescente
vetor3 = sorted(vetor1 + vetor2, reverse=True)

# Imprimimos o vetor 3 ordenado de maneira decrescente
print("\nVetor 3 ordenado de maneira decrescente:")
for elemento in vetor3:
    print(elemento)