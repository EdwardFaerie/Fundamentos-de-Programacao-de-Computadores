# Faça um programa que preencha um vetor com dez números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor.

# Cria uma lista vazia para armazenar os números digitados pelo usuário
números = []

# Loop que irá rodar 10 vezes para solicitar 10 números ao usuário
for i in range(10):
    # Solicita um número ao usuário e o converte para float (número decimal)
    # e adiciona à lista de números
    números.append(float(input("Digite um número: ")))

# Inicializa variáveis para contar os números negativos e somar os positivos
contagem_negativos = 0
soma_positivos = 0

# Loop que irá percorrer a lista de números
for num in números:
    # Verifica se o número é negativo
    if num < 0:
        # Incrementa a contagem de números negativos
        contagem_negativos += 1
    # Verifica se o número é positivo
    elif num > 0:
        # Soma o número positivo à variável soma_positivos
        soma_positivos += num

# Imprime os resultados
print("Quantidade de números negativos:", contagem_negativos)
print("Soma dos números positivos:", soma_positivos)