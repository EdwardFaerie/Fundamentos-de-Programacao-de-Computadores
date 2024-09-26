# Uma pequena loja de artesanato possui um vendedor e comercializa dez tipos de objetos, o vendedor recebe um salário de R$ 545,00 acrecido de 5% do total de suas vendas. Crie um programa que receba os preços e as quantidades vendidas e mostre um relatório contendo: Quantidade vendida, preço por unidade, valor total de cada produto, valor de comissão, produto mais vendido e a posição no vetor do produto mais vendido.

# Crie uma lista vazia para armazenar os produtos
products = []

# Loop para preencher a lista com 10 produtos
for num in range(1, 11):
    # Pede ao usuário que digite o total de vendas e o preço por unidade do produto
    # e armazena na lista como uma lista de 4 elementos: nome do produto, quantidade vendida, preço por unidade e estoque (fixo em 10)
    products = products + [[f"Product {num}", int(input(f"Total de Vendas do produto {num}: ")), int(input(f"Preço por unidade do produto {num}: ")), 10]]

# Função para calcular o valor total de vendas de todos os produtos
def total_sales_value(products):
    # Soma o preço por unidade de cada produto multiplicado pela quantidade vendida
    return sum(product[1] * product[2] for product in products)

# Função para calcular o valor da comissão
def commission_value(total_sales):
    # Retorna o valor da comissão fixo (R$ 545) mais 5% do valor total de vendas
    return 545 + total_sales * 0.05

# Função para encontrar o produto mais vendido
def best_selling_product(products):
    # Encontra a quantidade máxima vendida entre todos os produtos
    max_quantity = max(product[1] for product in products)
    # Filtra a lista de produtos para encontrar os que têm a quantidade máxima vendida
    best_selling_products = [product for product in products if product[1] == max_quantity]
    # Retorna o primeiro produto da lista de produtos mais vendidos
    return best_selling_products[0]

# Crie um dicionário para armazenar o relatório
report = {
    # Quantidade de cada produto
    "Quantidade de cada produto ": [product[1] for product in products],
    # Preço por unidade de cada produto
    "Preço por unidade ": [product[2] for product in products],
    # Valor total de cada produto (não utilizado)
    "Valor total de cada produto ": [product[3] for product in products],
    # Valor total de vendas de todos os produtos
    "Total de vendas de cada produto ": total_sales_value(products),
    # Valor da comissão
    "Valor de Comissão R$": commission_value(total_sales_value(products)),
    # Produto mais vendido
    "Produto mais vendido: ": best_selling_product(products)[0],
    # Posição do produto mais vendido na lista de produtos
    "Posição no vetor do produto mais vendido": products.index(best_selling_product(products))
}

# Imprime o relatório
for key, value in report.items():
    print(f"{key}: {value}")