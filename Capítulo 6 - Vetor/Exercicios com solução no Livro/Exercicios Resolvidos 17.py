# Faça um programa que receba seis números inteiros e mostre: os números pares digitados, a soma dos números pares digitados, os números ímpares digitados e a quantidade de números ímpares digitados.

# Lista vazia para armazenar os números digitados
numbers = [int(input("Digite um número: ")) for i in range(0,6)]

# Listas vazias para armazenar os números pares e ímpares
pares = []
impares = []

# Loop para separar os números em pares e ímpares
for num in numbers:
    # Verifica se o número é par
    if num % 2 == 0:
        # Se for par, adiciona o número à lista de pares
        pares.append(num)
    else:
        # Se for ímpar, adiciona o número à lista de ímpares
        impares.append(num)

# Calcula a soma dos números pares
soma_pares = sum(pares)

# Imprime os resultados
print("Números pares digitados:", pares)
print("Soma dos números pares digitados:", soma_pares)
print("Números ímpares digitados:", impares)
print("Quantidade de números ímpares digitados:", len(impares))

# Observação: O código utiliza a função sum para calcular a soma dos números pares e o operador % para verificar se um número é par ou ímpar. Além disso, o uso do len permite calcular a quantidade de números ímpares digitados.