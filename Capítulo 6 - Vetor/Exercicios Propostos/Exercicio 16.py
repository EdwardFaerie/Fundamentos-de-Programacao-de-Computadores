# Faça um programa que receba o nome de cinco produtos e seus respectivos preços. Calcule e mostre: ■ a quantidade de produtos com preço inferior a R$ 50,00; ■ o nome dos produtos com preço entre R$ 50,00 e R$ 100,00; ■ a média dos preços dos produtos com preço superior a R$ 100,00

# Inicializamos um vetor vazio para armazenar os produtos
produtos = []

# Loop para coletar informações de 5 produtos
for i in range(5):
    # Pedimos o nome do produto
    nome = input("Digite o nome do {}º produto: ".format(i+1))
    
    # Pedimos o preço do produto
    preco = float(input("Digite o preço do {}: R$ ".format(nome)))
    
    # Adicionamos o produto ao vetor como uma tupla (nome, preco)
    produtos.append((nome, preco))

# Imprimimos o relatório de preços
print("\nRelatório de preços:")

# Separamos os produtos em categorias
produtos_baratos = [produto for produto, preco in produtos if preco < 50]
produtos_medios = [produto for produto, preco in produtos if 50 <= preco <= 100]
produtos_caros = [produto for produto, preco in produtos if preco > 100]

# Imprimimos a quantidade de produtos com preço inferior a R$ 50,00
print("Quantidade de produtos com preço inferior a R$ 50,00: {}".format(len(produtos_baratos)))

# Verificamos se há produtos com preço entre R$ 50,00 e R$ 100,00
if produtos_medios:
    print("Produtos com preço entre R$ 50,00 e R$ 100,00:")
    # Imprimimos os produtos com preço entre R$ 50,00 e R$ 100,00
    for produto in produtos_medios:
        print("• {}".format(produto))

# Verificamos se há produtos com preço superior a R$ 100,00
if produtos_caros:
    # Calculamos a soma dos preços dos produtos caros
    soma_precos = sum(preco for _, preco in produtos if preco > 100)
    
    # Calculamos a média dos preços dos produtos caros
    media_precos = soma_precos / len(produtos_caros)
    
    # Imprimimos a média dos preços dos produtos caros
    print("Média dos preços dos produtos com preço superior a R$ 100,00: R$ {:.2f}".format(media_precos))