# Faça um programa que preencha: ■ um vetor com os nomes de cinco produtos; ■ uma matriz 5 x 4 com os preços dos cinco produtos em quatro lojas diferentes; ■ outro vetor com o custo do transporte dos cinco produtos. O programa deverá preencher uma segunda matriz 5 x 4 com os valores dos impostos de cada produto, de acordo com a tabela a seguir O programa deverá mostrar, ainda, um relatório com o nome do produto, o número da loja onde o produto é encontrado, o valor do imposto a pagar, o custo de transporte, o preço e o preço final (preço acrescido do valor do imposto e do custo do transporte).

# Preencher o vetor com os nomes de cinco produtos
produtos = ["Produto 1", "Produto 2", "Produto 3", "Produto 4", "Produto 5"]
# Esse vetor armazena os nomes dos produtos que serão utilizados no programa

# Preencher a matriz 5 x 4 com os preços dos cinco produtos em quatro lojas diferentes
precos = [
    [10.0, 12.0, 11.0, 13.0],
    [15.0, 18.0, 17.0, 19.0],
    [20.0, 22.0, 21.0, 23.0],
    [25.0, 28.0, 27.0, 29.0],
    [30.0, 32.0, 31.0, 33.0]
]
# Essa matriz armazena os preços dos produtos em quatro lojas diferentes

# Preencher o vetor com o custo do transporte dos cinco produtos
custo_transporte = [1.0, 2.0, 3.0, 4.0, 5.0]
# Esse vetor armazena o custo de transporte dos produtos

# Tabela de impostos
impostos = [
    [0.10, 0.15, 0.20, 0.25],
    [0.12, 0.18, 0.22, 0.28],
    [0.15, 0.20, 0.25, 0.30],
    [0.18, 0.22, 0.28, 0.32],
    [0.20, 0.25, 0.30, 0.35]
]
# Essa tabela armazena os impostos que serão aplicados aos produtos

# Preencher a segunda matriz 5 x 4 com os valores dos impostos de cada produto
impostos_calculados = [[0.0 for _ in range(4)] for _ in range(5)]
# Essa matriz armazena os impostos calculados para cada produto

# Calcular os impostos de cada produto
for i in range(5):
    for j in range(4):
        impostos_calculados[i][j] = precos[i][j] * impostos[i][j]
# Esse loop calcula os impostos de cada produto multiplicando o preço do produto pelo imposto correspondente

# Mostrar o relatório
print("Relatório:")
# Esse loop mostra o relatório com os dados calculados

for i in range(5):
    for j in range(4):
        preco_final = precos[i][j] + impostos_calculados[i][j] + custo_transporte[i]
        # Esse loop calcula o preço final do produto somando o preço, o imposto e o custo de transporte
        print(f"Produto: {produtos[i]}, Loja: {j+1}, Imposto: {impostos_calculados[i][j]:.2f}, Custo de Transporte: {custo_transporte[i]:.2f}, Preço: {precos[i][j]:.2f}, Preço Final: {preco_final:.2f}")
        # Esse print mostra os dados do relatório