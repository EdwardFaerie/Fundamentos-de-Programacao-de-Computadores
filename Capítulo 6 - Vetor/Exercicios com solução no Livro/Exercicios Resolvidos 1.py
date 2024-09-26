# Faça um programa que preencha um vetor com 9 números inteiros, calcule e mostre os números primos e suas respectivas posições

# Crie uma lista vazia para armazenar os números primos encontrados
lista_primos = []
# Crie uma lista vazia para armazenar os 9 números inteiros digitados pelo usuário
lista = []

# Loop para preencher a lista com 9 números inteiros digitados pelo usuário
for indice in range(0,9):
    # Pede ao usuário que digite um número inteiro e armazena na lista
    lista.append(int(input(f"Digite o {indice} com Número: ")))
cont = 0  # Variável não utilizada no código, pode ser removida

# Função para verificar se um número é primo
def is_prime(number):
    # Se o número for menor que 2, não é primo
    if number < 2:
        return False
    # Verifica se o número é divisível por qualquer número entre 2 e a raiz quadrada do número
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            # Se encontrar um divisor, o número não é primo
            return False
    # Se não encontrar nenhum divisor, o número é primo
    return True

# Loop para verificar quais números na lista são primos
for indice, valor in enumerate(lista):    
    # Chama a função is_prime para verificar se o valor é primo
    returned = is_prime(valor)
    if returned == True:
        # Se o valor for primo, adiciona à lista de primos
        lista_primos.append(valor)

# Imprime a lista original
print(f"Lista: {lista}")
# Imprime a lista de primos, se houver algum
if lista_primos != []:
    print(f"Lista de primos: {lista_primos}")