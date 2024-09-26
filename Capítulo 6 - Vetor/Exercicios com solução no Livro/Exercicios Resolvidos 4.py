# Faça um programa que preencha um vetor com oito números inteiros, calcule e mostre dois vetores, um vetor com valores positivos e outro com valores negativos

# Importa a função randint do módulo random para gerar números aleatórios
from random import randint

# Crie duas listas vazias para armazenar os números positivos e negativos
numbers = []
numbers_negative = []

# Loop para gerar 9 números aleatórios entre 0 e 10 e armazená-los na lista numbers
for i in range(0, 9):
    numbers = numbers + [randint(0, 10)]

# Loop para criar a lista numbers_negative com os valores negativos correspondentes à lista numbers
for index, value in enumerate(numbers):
    # Calcula o valor negativo do número positivo
    negative = value * -1
    # Insere o valor negativo na lista numbers_negative na mesma posição que o valor positivo
    numbers_negative.insert(index, negative)

# Imprime as listas de números positivos e negativos
print(f'Numeros Positivos: {numbers}')
print(f'Numeros negativos: {numbers_negative}')

print('\n')

# Loop para imprimir os valores e suas posições na lista numbers
for index, value in enumerate(numbers):
    print(f'Positivos Posição: {index} tem o valor: {value}')

# Loop para imprimir os valores e suas posições na lista numbers_negative
for index, value in enumerate(numbers_negative):
    print(f'Negativos Posição: {index} tem o valor: {value}')