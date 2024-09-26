# Faça um programa que preencha três vetores com dez posições cada um: o primeiro vetor, com os nomes de dez produtos; o segundo vetor, com os códigos dos dez produtos; e o terceiro vetor, com os preços dos produtos. Mostre um relatório apenas com o nome, o código, o preço e o novo preço dos produtos que sofrerão aumento. Sabe-se que os produtos que sofrerão aumento são aqueles que possuem código par ou preço superior a R$ 1.000,00. Sabe-se ainda que, para os produtos que satisfazem as duas condições anteriores, código e preço, o aumento será de 20%; para aqueles que satisfazem apenas a condição de código, o aumento será de 15%; e para aqueles que satisfazem apenas a condição de preço, o aumento será de 10%.

# Cria listas vazias para armazenar os nomes, códigos e preços dos produtos
nomes_produtos = []
codigos_produtos = []
precos_produtos = []

# Loop que irá rodar 10 vezes para solicitar informações de 10 produtos
for i in range(10):
    # Solicita o nome do produto e o adiciona à lista de nomes
    nomes_produtos.append(input("Digite o nome do produto {}: ".format(i+1)))
    # Solicita o código do produto e o adiciona à lista de códigos
    codigos_produtos.append(int(input("Digite o código do produto {}: ".format(i+1))))
    # Solicita o preço do produto e o adiciona à lista de preços
    precos_produtos.append(float(input("Digite o preço do produto {}: ".format(i+1))))

# Imprime o relatório de produtos com aumento
print("Relatório de produtos com aumento:")
for i in range(10):
    # Verifica se o produto tem código par ou preço maior que 1000
    if codigos_produtos[i] % 2 == 0 or precos_produtos[i] > 1000:
        # Aplica aumento de preço de acordo com as regras
        if codigos_produtos[i] % 2 == 0 and precos_produtos[i] > 1000:
            # Aumento de 20% para produtos com código par e preço maior que 1000
            novo_preco = precos_produtos[i] * 1.20
        elif codigos_produtos[i] % 2 == 0:
            # Aumento de 15% para produtos com código par
            novo_preco = precos_produtos[i] * 1.15
        else:
            # Aumento de 10% para produtos com preço maior que 1000
            novo_preco = precos_produtos[i] * 1.10
        # Imprime o relatório do produto com o novo preço
        print("Nome: {}, Código: {}, Preço: R$ {:.2f}, Novo Preço: R$ {:.2f}".format(nomes_produtos[i], codigos_produtos[i], precos_produtos[i], novo_preco))