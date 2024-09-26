# Faça um programa que gera duas listas de 20 caracteres aleatórios, respectivamente chamadas de A e B. A seguir troque o elemento da lista A com o 20º de B e assim por diante até trocar o 20º de A com o 1º de B. Mostre os vetores antes e depois da troca

# Importa as bibliotecas necessárias
import random
import string

# Gera duas listas de 20 letras aleatórias
A = [random.choice(string.ascii_letters) for _ in range(20)]
B = [random.choice(string.ascii_letters) for _ in range(20)]

# Imprime as listas antes da troca
print("Antes da troca:")
print("A:", A)
print("B:", B)

# Loop para trocar os elementos das listas
for i in range(20):
    # Troca o elemento i da lista A com o elemento 19-i da lista B
    A[i], B[19 - i] = B[19 - i], A[i]

# Imprime as listas depois da troca
print("\nDepois da troca:")
print("A:", A)
print("B:", B)

# Observação: O código utiliza a função random.choice para gerar letras aleatórias da tabela ASCII. Além disso, o uso do loop for permite trocar os elementos das listas de forma eficiente. A troca é feita utilizando a sintaxe A[i], B[19 - i] = B[19 - i], A[i], que é uma forma concisa de trocar os valores de duas variáveis.