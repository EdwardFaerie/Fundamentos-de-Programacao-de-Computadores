# Faça um programa que leia um vetor com quinze posições para números inteiros. Depois da leitura, divida todos os seus elementos pelo maior valor do vetor. Mostre o vetor após os cálculos.

# Inicializamos um vetor vazio para armazenar os elementos
vetor = []

# Preenchemos o vetor com 15 elementos
print("Preencha o vetor:")
for i in range(15):
    # Pedimos o elemento ao usuário
    elemento = int(input("Digite o {}º elemento: ".format(i+1)))
    
    # Adicionamos o elemento ao vetor
    vetor.append(elemento)

# Encontramos o maior valor no vetor
maior_valor = max(vetor)

# Verificamos se o maior valor é diferente de zero
if maior_valor != 0:
    # Dividimos cada elemento do vetor pelo maior valor
    vetor_dividido = [elemento / maior_valor for elemento in vetor]
else:
    # Se o maior valor for zero, não é possível dividir por zero
    print("Erro: não é possível dividir por zero!")

# Imprimimos o vetor após os cálculos
print("\nVetor após os cálculos:")
print(vetor_dividido)