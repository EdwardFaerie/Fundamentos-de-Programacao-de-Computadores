# Faça um programa que preencha um vetor com seis elementos númericos inteiros. Calcule e mostre: Todos os números Pares, a quantidade de números pares; Todos os números ímpares, a quantidade de números ímpares

# Pede ao usuário inserir numeros inteiros 6 vezes
vetor = [int(input(f"Digite o {i+1}º número: ")) for i in range(6)]

# Pode se escrever também destá forma o código acima:

# vetor = []
# for i in range(0,6):
#   vetor.append(f"DIgite o {i+1}º número: ")

# Criar as listas de pares e impares
pares = []
impares = []

# Criar valores de quantidades de pares e impares
qtd_pares = 0
qtd_impares = 0

# Para cada número no vetor
for num in vetor:
    if num % 2 == 0: # Se o restante do número dividido por 2 for 0 então é par
        pares.append(num) # Adicionar na lista de pares
        qtd_pares += 1 # Mais um para a quantidade de pares
    else: # caso o restante não for 0 então é ímpar
        impares.append(num) # Adicionar na lista de ímpares
        qtd_impares += 1 # Mais um para a quantidade de ímpares

# Mostrar os valores resultantes de cada um
print("Números pares:", pares)
print("Quantidade de números pares:", qtd_pares)
print("Números ímpares:", impares)
print("Quantidade de números ímpares:", qtd_impares)