# Faça um programa que preencha um vetor com 10 números inteiros e um segundo com cinco números inteiros. Calcule e mostre dois vetores resultantes, o primeiro resultante será composto pelos números pares gerado do primeiro vetor somado a todos os elementos do segundo vetor o segundo resultante será composto pelos números ímpares gerados pelo elemento do primeiro vetor somado a todos os elementosdo segundo vetor

# Listas vazias para armazenar os números inteiros
vector1 = []
vector2 = []

# Loop para preencher a primeira lista com 10 números inteiros
for _ in range(10):
    # Pede ao usuário que digite um número inteiro
    vector1.append(int(input("Digite um número Inteiro da primeira lista: ")))

# Loop para preencher a segunda lista com 5 números inteiros
for _ in range(5):
    # Pede ao usuário que digite um número inteiro
    vector2.append(int(input("Digite um número Inteiro da segunda lista: ")))

# Listas vazias para armazenar os resultados
result_vector_pares = []
result_vector_impares = []

# Loop para processar os números da primeira lista
for num in vector1:
    # Verifica se o número é par
    if num % 2 == 0:
        # Se for par, adiciona o número somado com a soma da segunda lista à lista de resultados pares
        result_vector_pares.append(num + sum(vector2))
    else:
        # Se for ímpar, adiciona o número somado com a soma da segunda lista à lista de resultados ímpares
        result_vector_impares.append(num + sum(vector2))

# Imprime as listas
print("Vetor 1:", vector1)
print("Vetor 2:", vector2)
print("Vetor (Pares):", result_vector_pares)
print("Vetor (Ímpares):", result_vector_impares)

# Observação: O código utiliza a função sum para calcular a soma da segunda lista e adiciona essa soma a cada número da primeira lista. Além disso, o uso do operador % permite verificar se um número é par ou ímpar.