# Faça um programa que gere os dez primeiros números primos acima de 100 e armazeneos em um vetor. Escreva no final o vetor resultante

# Função para verificar se um número é primo
def is_prime(n):
    # Verifica se o número é menor ou igual a 1
    if n <= 1:
        # Se sim, retorna False (não é primo)
        return False
    # Loop para verificar se o número é divisível por algum número entre 2 e a raiz quadrada de n
    for i in range(2, int(n ** 0.5) + 1):
        # Verifica se o número é divisível por i
        if n % i == 0:
            # Se sim, retorna False (não é primo)
            return False
    # Se o número não é divisível por nenhum número entre 2 e a raiz quadrada de n, retorna True (é primo)
    return True

# Lista vazia para armazenar os números primos
primes = []
# Número inicial para começar a busca por números primos
num = 101
# Loop para encontrar os 10 primeiros números primos a partir de num
while len(primes) < 10:
    # Verifica se o número atual é primo
    if is_prime(num):
        # Se sim, adiciona o número à lista de primos
        primes.append(num)
    # Incrementa o número atual
    num += 1

# Imprime a lista de números primos
print(primes)

# Observação: O código utiliza uma função is_prime para verificar se um número é primo e um loop para encontrar os 10 primeiros números primos a partir de um número inicial. A lista primes é utilizada para armazenar os números primos encontrados.