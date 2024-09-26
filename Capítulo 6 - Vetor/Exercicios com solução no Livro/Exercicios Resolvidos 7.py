# Faça um programa que calcula e mostra um vetor em ordem crescente de um outro vetor de 8 valores de entrada.

# Crie um vetor vazio para armazenar os números digitados pelo usuário
Vetor = []

# Loop para preencher o vetor com 8 números digitados pelo usuário
for num in range(0, 8):
    # Pede ao usuário que digite um número para a posição atual
    Vetor = Vetor + [int(input(f"Escreva um número para a posição {num}: "))]

# Ordena o vetor em ordem crescente usando a função sorted
vetor_sorted = sorted(Vetor)

# Imprime o vetor original e o vetor ordenado
print(f"Vetor não Organizado {Vetor}")
print(f"Vetor Organizado {vetor_sorted}")