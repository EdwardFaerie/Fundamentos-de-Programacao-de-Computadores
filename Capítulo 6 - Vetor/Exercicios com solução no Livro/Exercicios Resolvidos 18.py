# Faça um programa que receba um número sorteado por um dado em vinte jogadas. Mostre os números sorteados e a frequencia que aparecem.

# Importa a biblioteca random para gerar números aleatórios
import random

# Lista vazia para armazenar os números rolados
rolled_numbers = []

# Loop para gerar 20 números aleatórios entre 1 e 6
for _ in range(20):
    # Gera um número aleatório entre 1 e 6 e adiciona à lista
    rolled_numbers.append(random.randint(1, 6))
    
# Dicionário vazio para armazenar a frequência de cada número
frequency = {}

# Loop para calcular a frequência de cada número
for num in rolled_numbers:
    # Verifica se o número já está no dicionário
    if num in frequency:
        # Se sim, incrementa a frequência do número
        frequency[num] += 1
    else:
        # Se não, adiciona o número ao dicionário com frequência 1
        frequency[num] = 1

# Imprime os resultados
print("Números na rolagem:")
print(rolled_numbers)
print("\nFrequencia de cada número:")
for num, freq in frequency.items():
    # Imprime o número e sua frequência
    print(f"{num}: {freq} Vezes")

# Observação: O código utiliza a função random.randint para gerar números aleatórios entre 1 e 6. Além disso, o uso do dicionário frequency permite calcular a frequência de cada número de forma eficiente.