# Faça um programa que leia um vetor com dez posições para números inteiros e mostre somente os números positivos. 

# Inicializamos um vetor vazio para armazenar os elementos
vetor = []

# Preenchemos o vetor com 10 elementos
print("Preencha o vetor:")
for i in range(10):
    # Pedimos o elemento ao usuário
    elemento = int(input("Digite o {}º elemento: ".format(i+1)))
    
    # Adicionamos o elemento ao vetor
    vetor.append(elemento)

# Imprimimos os números positivos do vetor
print("\nNúmeros positivos do vetor:")
for elemento in vetor:
    # Verificamos se o elemento é positivo
    if elemento > 0:
        # Imprimimos o elemento positivo
        print(elemento)