# Faça um programa que preencha: ■ um vetor com oito posições, contendo nomes de lojas; ■ outro vetor com quatro posições, com nomes de produtos; ■ uma matriz com os preços de todos os produtos em cada loja. O programa deverá mostrar todas as relações (nome do produto — nome da loja) em que o preço não ultrapasse R$ 120,00.

# Defina um vetor com oito posições, contendo nomes de lojas
lojas = ["Loja 1", "Loja 2", "Loja 3", "Loja 4", "Loja 5", "Loja 6", "Loja 7", "Loja 8"]

# Defina outro vetor com quatro posições, com nomes de produtos
produtos = ["Produto A", "Produto B", "Produto C", "Produto D"]

# Defina uma matriz com os preços de todos os produtos em cada loja
# A matriz terá 8 linhas (lojas) e 4 colunas (produtos)
precos = [
    [100, 120, 90, 110],  # Preços dos produtos na Loja 1
    [130, 90, 100, 120],  # Preços dos produtos na Loja 2
    [110, 100, 90, 130],  # Preços dos produtos na Loja 3
    [120, 110, 100, 90],  # Preços dos produtos na Loja 4
    [90, 120, 110, 100],  # Preços dos produtos na Loja 5
    [100, 90, 120, 110],  # Preços dos produtos na Loja 6
    [110, 130, 100, 120],  # Preços dos produtos na Loja 7
    [120, 100, 90, 110]   # Preços dos produtos na Loja 8
]

# Mostrar todas as relações (nome do produto — nome da loja) em que o preço não ultrapasse R$ 120,00
for i in range(len(lojas)):  # Percorra as lojas
    for j in range(len(produtos)):  # Percorra os produtos
        if precos[i][j] <= 120:  # Verifique se o preço é menor ou igual a R$ 120,00
            print(f"{produtos[j]} - {lojas[i]}: R$ {precos[i][j]:.2f}")  # Imprima a relação