# Faça um programa que preencha um vetor com dez números inteiros e um segundo vetor com cinco números inteiros, calcule e mostre dois vetores resultantes. O primeiro vetor resultante será composto pela soma de cada número par do primeiro vetor somado a todos os números do segundo vetor. O segundo vetor resultante será composto pela quantidade de divisores que cada número ímpar do primeiro vetor tem no segundo vetor.

# Cria listas vazias para armazenar os números inteiros dos vetores
vetor1 = []
vetor2 = []

# Loop que irá rodar 10 vezes para solicitar números inteiros para o vetor1
for i in range(10):
    # Solicita um número inteiro e o adiciona ao vetor1
    vetor1.append(int(input("Digite o número inteiro {}: ".format(i+1))))

# Loop que irá rodar 5 vezes para solicitar números inteiros para o vetor2
for i in range(5):
    # Solicita um número inteiro e o adiciona ao vetor2
    vetor2.append(int(input("Digite o número inteiro {}: ".format(i+1))))

# Cria listas vazias para armazenar os resultados
vetor_resultante1 = []
vetor_resultante2 = []

# Loop que irá percorrer os números inteiros do vetor1
for num in vetor1:
    # Verifica se o número é par
    if num % 2 == 0:
        # Calcula a soma do número com a soma dos números do vetor2
        soma = num + sum(vetor2)
        # Adiciona a soma ao vetor_resultante1
        vetor_resultante1.append(soma)
    else:
        # Inicializa o contador de divisores
        divisores = 0
        # Loop que irá percorrer os números inteiros do vetor2
        for num2 in vetor2:
            # Verifica se o número é divisor do número atual do vetor1
            if num % num2 == 0:
                # Incrementa o contador de divisores
                divisores += 1
        # Adiciona o contador de divisores ao vetor_resultante2
        vetor_resultante2.append(divisores)

# Imprime os resultados
print("Vetor resultante 1:", vetor_resultante1)
print("Vetor resultante 2:", vetor_resultante2)