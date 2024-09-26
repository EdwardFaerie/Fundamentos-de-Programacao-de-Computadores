# Faça um programa que leia um conjunto de 15 valores e armazena-os em um vetor. A seguir separe-os em dois outros vetores P e I com 5 posições cada. Vetor P armazena números pares e o Vetor I os números ímpares. Como o tamanho dos vetores não pode ser suficiente para armazenar os números deve-se sempre verificar se já estão cheios. Caso P ou I estejam cheios deve se mostrálos e recomeçar o preenchimento da primeira posição. Terminando o processamento, mostre o conteudo restante dentro dos vetores P e I

# Lista vazia para armazenar os números
lista = [float(input(f"Digite um número para a posição {i}: ")) for i in range(0, 15)]

# Listas vazias para armazenar os números pares e ímpares
P = []
I = []

# Loop para processar os números da lista
for valor in lista:
    # Verifica se as listas P e I estão cheias
    if len(P) == 5 and len(I) == 5:
        # Se sim, imprime as listas e reinicia-as
        print("Listas P e I cheias")
        print(f"Lista P: {P}")
        print(f"Lista I: {I}")
        P = []
        I = []

    # Verifica se o número é par
    if valor % 2 == 0:
        # Se sim, adiciona o número à lista P se ela não estiver cheia
        if len(P) < 5:
            P.append(valor)
        else:
            # Se a lista P estiver cheia, imprime a lista e reinicia-a
            print("Lista P cheia")
            print(f"Lista P: {P}")
            P = [valor]
    else:
        # Se o número for ímpar, adiciona o número à lista I se ela não estiver cheia
        if len(I) < 5:
            I.append(valor)
        else:
            # Se a lista I estiver cheia, imprime a lista e reinicia-a
            print("Lista I cheia")
            print(f"Lista I: {I}")
            I = [valor]

# Imprime as listas finais
print(f"Lista P: {P}")
print(f"Lista I: {I}")

# Observação: O código utiliza um loop para processar os números da lista e adicioná-los às listas P e I. Se as listas estiverem cheias, elas são impressas e reiniciadas. O código também verifica se os números são pares ou ímpares e adiciona-os às listas correspondentes.