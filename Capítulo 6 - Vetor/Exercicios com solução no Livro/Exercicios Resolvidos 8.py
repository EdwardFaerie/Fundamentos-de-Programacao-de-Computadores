# Faça um programa que preencha dois vetores com cinco elementos cada e depois ordene-os de forma crescente, gere um terceito vetor com dez posições composto pela junçao dos dois vetores anteriores e também organizado de forma crescente

# Crie três vetores vazios para armazenar os números digitados pelo usuário
vetor1 = []
vetor2 = []
vetor3 = []

# Loop para preencher o vetor1 com 5 números digitados pelo usuário
for num in range(0, 5):
    # Pede ao usuário que digite um número para a posição atual
    vetor1 = vetor1 + [int(input(f"Valor da lista 1 com posição {num}: "))]
    
# Loop para preencher o vetor2 com 5 números digitados pelo usuário
for num in range(0, 5):
    # Pede ao usuário que digite um número para a posição atual
    vetor2 = vetor2 + [int(input(f"Valor da lista 2 com posição {num}: "))]

# Crie o vetor3 como a concatenação de vetor1 e vetor2
vetor3 = list(vetor1 + vetor2)

# Ordena os vetores em ordem crescente usando a função sorted
vetor3 = sorted(vetor3)
vetor2 = sorted(vetor2)
vetor1 = sorted(vetor1)

# Imprime os vetores ordenados
print(f"Vetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}")
print(f"Vetor 3: {vetor3}")