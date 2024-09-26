# Faça um programa que leia um vetor A de dez posições cotendo números inteiros, determine e mostre a seguir os elementos de A e quantas vezes cada um se repete.

# Lista vazia para armazenar os números
A = [0] * 10

# Loop para preencher a lista com números
for i in range(10):
    # Pede ao usuário que digite o valor da posição i+1
    A[i] = int(input(f"Digite o valor da posição {i+1}: "))

# Dicionário vazio para armazenar as frequências dos números
frequencia = {}

# Loop para calcular as frequências dos números
for elemento in A:
    # Verifica se o número já está no dicionário
    if elemento in frequencia:
        # Se sim, incrementa a frequência do número
        frequencia[elemento] += 1
    else:
        # Se não, adiciona o número ao dicionário com frequência 1
        frequencia[elemento] = 1

# Imprime as frequências dos números
print("Frequências dos números:")
for elemento, freq in frequencia.items():
    # Imprime o número e sua frequência
    print(f"O Número {elemento} Aparece {freq} vezes.")

# Observação: O código utiliza um loop para preencher a lista com números e outro loop para calcular as frequências dos números. O dicionário frequencia é utilizado para armazenar as frequências dos números, onde cada chave é um número e o valor é a frequência desse número.