# Faça um programa que mostre um vetor resultante da intercalação de outros dois vetores definidos

# Duas listas de números
lista1 = [3, 5, 4, 2, 2, 5, 3, 2, 5, 9]
lista2 = [7, 15, 20, 0, 18, 4, 55, 23, 8, 6]

# Crie uma lista que intercala os elementos das duas listas
# usando a função zip para criar pares de elementos e uma lista de compreensão para "desempacotar" os pares
interleaved_list = [x for pair in zip(lista1, lista2) for x in pair]

# Imprime a lista intercalada
print(interleaved_list)