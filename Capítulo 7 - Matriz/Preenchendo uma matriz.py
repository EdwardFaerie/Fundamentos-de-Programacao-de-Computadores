# Crie uma matriz matriz_B com três linhas, onde cada linha é uma cópia do vetor vetor_A que é incrementado em cada iteração do loop.

# Inicializa uma lista vazia para a matriz B
matriz_B = []

# Inicializa uma lista vazia para o vetor A
vetor_A = []

# Loop que irá rodar 3 vezes
for i in range(0,3):
    # Adiciona o valor de i ao vetor A
    vetor_A.append(i)
    
    # Adiciona uma cópia do vetor A à matriz B (usando slicing [:])
    matriz_B.append(vetor_A[:])

# Imprime a matriz B
print(f"{matriz_B}")