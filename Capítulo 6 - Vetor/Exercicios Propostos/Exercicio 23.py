# Faça um programa que leia dois vetores (A e B) com cinco posições para números inteiros. O programa deve, então, subtrair o primeiro elemento de A do último de B, acumulando o valor, subtrair o segundo elemento de A do penúltimo de B, acumulando o valor e assim por diante. Ao final, mostre o resultado de todas as subtrações realizadas.

# Inicializamos três variáveis: dois vetores vazios e uma variável para armazenar o resultado
vetor_A = []
vetor_B = []
resultado = 0

# Preenchemos o vetor A com 5 elementos
print("Preencha o vetor A:")
for i in range(5):
    # Pedimos o elemento ao usuário
    elemento = int(input("Digite o {}º elemento: ".format(i+1)))
    
    # Adicionamos o elemento ao vetor A
    vetor_A.append(elemento)

# Preenchemos o vetor B com 5 elementos
print("\nPreencha o vetor B:")
for i in range(5):
    # Pedimos o elemento ao usuário
    elemento = int(input("Digite o {}º elemento: ".format(i+1)))
    
    # Adicionamos o elemento ao vetor B
    vetor_B.append(elemento)

# Realizamos as subtrações entre os elementos do vetor B e do vetor A, começando do final do vetor B
for i in range(5):
    # Subtraímos o elemento do vetor A do elemento correspondente do vetor B, começando do final do vetor B
    resultado += vetor_B[4-i] - vetor_A[i]

# Imprimimos o resultado das subtrações
print("\nResultado das subtrações:")
print(resultado)