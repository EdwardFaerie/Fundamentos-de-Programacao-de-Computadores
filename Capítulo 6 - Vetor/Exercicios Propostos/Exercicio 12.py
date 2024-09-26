# Faça um programa que receba cinco números e mostre a saída a seguir: Digite o 1º número 5 Digite o 2º número 3 Digite o 3º número 2 Digite o 4º número 0 Digite o 5º número 2 Os números digitados foram: 5 + 3 + 2 + 0 + 2 = 12

# Cria uma lista vazia para armazenar os números
numeros = []

# Loop que irá rodar 5 vezes para solicitar números
for i in range(5):
    # Solicita um número e o adiciona à lista
    numeros.append(int(input("Digite o {}º número ".format(i+1))))

# Calcula a soma dos números da lista
soma = sum(numeros)

# Imprime os resultados
print("Os números digitados foram:", end=" ")
for num in numeros:
    # Imprime cada número seguido de "+"
    print(num, end=" + ")
# Remove os últimos dois caracteres (" + ") e imprime a soma
print("\b\b= ", soma)