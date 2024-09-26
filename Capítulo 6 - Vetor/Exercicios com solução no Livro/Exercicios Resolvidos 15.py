# Faça um programa que preencha um primeiro vetor com dez números inteiros e um segundo com 5 números inteiros. O programa deverá mostrar uma lista dos números do vetor com seus respectivos divisores armazenados no segundo vetor, bem como suas posições.

# Listas vazias para armazenar os números e os divisores
vetor1 = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]
vetor2 = [int(input(f"Digite o {i+1}º divisor: ")) for i in range(5)]

# Loop para encontrar os divisores de cada número no vetor1
for i, num in enumerate(vetor1):
    # Utiliza uma lista de compreensão para encontrar os divisores do número atual
    divisores = [div for div in vetor2 if num % div == 0]
    # Imprime o número e seus divisores
    print(f"O número {num} na posição {i} tem os divisores: {divisores}")

# Observação: O código utiliza uma lista de compreensão para encontrar os divisores de cada número no vetor1. Isso é uma forma concisa e eficiente de realizar essa tarefa. Além disso, o uso do enumerate permite que você acesse tanto o índice quanto o valor de cada elemento no vetor1.