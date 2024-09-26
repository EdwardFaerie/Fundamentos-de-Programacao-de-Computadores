# Faça um programa que receba dez números inteiros e armazene-os em um vetor. Calcule e mostre dois vetores resultantes: o primeiro com os números pares e o segundo, com os números ímpares.

# Cria uma lista vazia para armazenar os números inteiros
vetor = []

# Loop que irá rodar 10 vezes para solicitar números inteiros
for i in range(10):
    # Solicita um número inteiro e o adiciona ao vetor
    vetor.append(int(input("Digite o número inteiro {}: ".format(i+1))))

# Cria listas compostas para separar os números pares e ímpares
vetor_pares = [num for num in vetor if num % 2 == 0]
vetor_impares = [num for num in vetor if num % 2 != 0]

# Imprime os resultados
print("Vetor de números pares:", vetor_pares)
print("Vetor de números ímpares:", vetor_impares)