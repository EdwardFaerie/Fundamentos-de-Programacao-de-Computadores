# Faça um programa que preencha um vetor com quinze números, determine e mostre: ■ o maior número e a posição por ele ocupada no vetor; ■ o menor número e a posição por ele ocupada no vetor.

# Inicializamos um vetor vazio para armazenar os elementos
vetor = []

# Preenchemos o vetor com 15 elementos
print("Preencha o vetor:")
for i in range(15):
    # Pedimos o elemento ao usuário
    elemento = int(input("Digite o {}º elemento: ".format(i+1)))
    
    # Adicionamos o elemento ao vetor
    vetor.append(elemento)

# Imprimimos o relatório do vetor
print("\nRelatório do vetor:")

# Encontramos o maior número no vetor
maior_numero = max(vetor)
posicao_maior = vetor.index(maior_numero)
print("Maior número: {} (posição {})".format(maior_numero, posicao_maior+1))

# Encontramos o menor número no vetor
menor_numero = min(vetor)
posicao_menor = vetor.index(menor_numero)
print("Menor número: {} (posição {})".format(menor_numero, posicao_menor+1))