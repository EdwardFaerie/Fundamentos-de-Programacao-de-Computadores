# Faça um programa que leia um vetor com dez posições para números inteiros. Crie um segundo vetor, substituindo os valores nulos por 1. Mostre os dois vetores.

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

# Imprimimos o vetor 1
print("\nVetor 1:")
for elemento in vetor1:
    print(elemento)

# Criamos o vetor 2 substituindo os zeros do vetor 1 por 1
vetor2 = [1 if elemento == 0 else elemento for elemento in vetor1]

# Imprimimos o vetor 2
print("\nVetor 2:")
for elemento in vetor2:
    print(elemento)