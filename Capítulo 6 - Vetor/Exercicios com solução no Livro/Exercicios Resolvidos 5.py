# Faça um programa que através de 2 vetores X e Y, mostre a união, diferença, soma, produto e intersecção dos dois vetores.

# Dois vetores de números
Vetor_X = [3, 8, 4, 2, 1, 6, 8, 7, 11, 9]
Vetor_Y = [2, 1, 5, 12, 3, 0, 1, 4, 5, 6]

# Crie um vetor de união entre Vetor_X e Vetor_Y
# usando a função set para remover duplicatas e converter para lista
vetor_uniao = list(set(Vetor_X + Vetor_Y))

# Crie um vetor de diferença entre Vetor_X e Vetor_Y
# usando a função set para remover duplicatas e converter para lista
vetor_diferenca = list(set(Vetor_X) - set(Vetor_Y))

# Crie vetores vazios para armazenar a soma e o produto elemento a elemento
vetor_soma = []
vetor_produto = []

# Loop para calcular a soma elemento a elemento entre Vetor_X e Vetor_Y
for index, value in enumerate(Vetor_X):
    valor_final = value + Vetor_Y[index]
    vetor_soma.append(valor_final)

# Loop para calcular o produto elemento a elemento entre Vetor_X e Vetor_Y
for index, value in enumerate(Vetor_X):
    valor_final = value * Vetor_Y[index]
    vetor_produto.append(valor_final)

# Crie um vetor de intersecção entre Vetor_X e Vetor_Y
# usando a função set para remover duplicatas e converter para lista
vetor_interseccao = list(set(Vetor_X) & set(Vetor_Y))

# Imprime os resultados
print(f"Vetor União: {vetor_uniao}")
print(f"Vetor Diferença: {vetor_diferenca}")
print(f"Vetor de Soma: {vetor_soma}")
print(f"Vetor de Produto: {vetor_produto}")
print(f"Vetor de Intersecção: {vetor_interseccao}")