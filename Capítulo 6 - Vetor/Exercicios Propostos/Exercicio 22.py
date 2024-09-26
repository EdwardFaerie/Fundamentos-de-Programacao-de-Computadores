# Faça um programa que leia um vetor A de dez posições. Em seguida, compacte o vetor, retirando os valores nulos e negativos. Armazene esse resultado no vetor B. Mostre o vetor B. (Lembre-se: o vetor B pode não ser completamente preenchido.)

# Inicializamos dois vetores vazios para armazenar os elementos
vetor_A = []
vetor_B = []

# Preenchemos o vetor A com 10 elementos
print("Preencha o vetor A:")
for i in range(10):
    # Pedimos o elemento ao usuário
    elemento = int(input("Digite o {}º elemento: ".format(i+1)))
    
    # Adicionamos o elemento ao vetor A
    vetor_A.append(elemento)

# Criamos o vetor B com os elementos positivos do vetor A
vetor_B = [elemento for elemento in vetor_A if elemento > 0]

# Imprimimos o vetor B
print("\nVetor B:")
for elemento in vetor_B:
    print(elemento)