# Faça um programa que preencha um vetor com dez números inteiros, calcule e mostre os números superiores a cinquenta e suas respectivas posições. O programa deverá mostrar uma mensagem se não existir nenhum número nesta condição.

# Listas vazias para armazenar os números inteiros e os números maiores que 50
numeros = []
numeros_maiores = []

# Loop para preencher a lista de números inteiros
while True:
    # Pede ao usuário que digite um valor
    numeros.append(int(input("Digite um valor: ")))
    # Verifica se a lista de números inteiros já tem 10 elementos
    if len(numeros) == 10:
        # Se sim, sai do loop
        break

# Loop para encontrar os números maiores que 50 na lista de números inteiros
for index, value in enumerate(numeros):
    # Verifica se o número atual é maior que 50
    if value > 50:
        # Se sim, adiciona o índice e o valor ao final da lista de números maiores
        numeros_maiores.append([index, value])

# Imprime a lista de números inteiros
print(f"Lista de números inteiros: {numeros}")

# Verifica se a lista de números maiores não está vazia
if numeros_maiores != []:
    # Se não está vazia, loop para imprimir os números maiores que 50 e suas posições
    for index, value in enumerate(numeros_maiores):
        # Imprime o número e sua posição na lista de números inteiros
        print(f"O número {value[1]} está na posição {numeros.index(value[1])}")
else:
    # Se está vazia, imprime a mensagem de que não existem números maiores que 50
    print(f"Não existem números maiores que 50!")