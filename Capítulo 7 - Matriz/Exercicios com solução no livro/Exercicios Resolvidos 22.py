# Faça um programa que receba o estoque atual de três produtos, armazenados em quatro armazéns, e coloque esses dados em uma matriz 5  3. Considerando que a última linha dessa matriz contenha o custo de cada produto, o programa deverá calcular e mostrar: ■ a quantidade de itens quadrados em cada armazém; ■ qual armazém possui maior estoque do produto 2; ■ qual armazém possui menor estoque; ■ qual o custo total de cada produto; ■ qual o custo total de cada armazém. Devem ser desconsiderados empates.

# Receber o estoque atual de três produtos, armazenados em quatro armazéns
estoque = []
for i in range(4):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Digite o estoque do produto {j+1} no armazém {i+1}: ")))
    estoque.append(linha)

# Receber o custo de cada produto
custo = []
for i in range(3):
    custo.append(int(input(f"Digite o custo do produto {i+1}: ")))

# Criar a matriz 5 x 3
matriz = estoque + [custo]

# Calcular a quantidade de itens quadrados em cada armazém
itens_quadrados = []
for i in range(4):
    itens_quadrados.append(sum(x**2 for x in matriz[i]))

# Calcular qual armazém possui maior estoque do produto 2
maior_estoque_produto2 = max(matriz[i][1] for i in range(4))

# Calcular qual armazém possui menor estoque
menor_estoque = min(sum(matriz[i]) for i in range(4))

# Calcular o custo total de cada produto
custo_total_produto = [sum(matriz[i][j] * matriz[4][j] for i in range(4)) for j in range(3)]

# Calcular o custo total de cada armazém
custo_total_armazem = [sum(matriz[i][j] * matriz[4][j] for j in range(3)) for i in range(4)]

# Mostrar os resultados
print("Quantidade de itens quadrados em cada armazém:", itens_quadrados)
print("Armazém com maior estoque do produto 2:", matriz.index(max(matriz, key=lambda x: x[1])) + 1)
print("Armazém com menor estoque:", matriz.index(min(matriz, key=sum)) + 1)
print("Custo total de cada produto:", custo_total_produto)
print("Custo total de cada armazém:", custo_total_armazem)