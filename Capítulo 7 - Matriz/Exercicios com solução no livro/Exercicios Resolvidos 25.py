# Elabore um programa que receba as vendas de cinco produtos em três lojas diferentes, e em dois meses consecutivos. O programa deverá armazenar essas vendas em duas matrizes 5 x 3. O bimestre é uma matriz 5 x 3, resultado da soma das duas matrizes anteriores. Deverá ainda calcular e mostrar: ■ as vendas de cada produto, em cada loja, no bimestre; ■ a maior venda do bimestre; ■ o total vendido, por loja, no bimestre; ■ o total vendido de cada produto no bimestre.

# Receber as vendas de cinco produtos em três lojas diferentes, em dois meses consecutivos
vendas_mes1 = []
for i in range(5):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Digite as vendas do produto {i+1} na loja {j+1} no mês 1: ")))
    vendas_mes1.append(linha)

vendas_mes2 = []
for i in range(5):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Digite as vendas do produto {i+1} na loja {j+1} no mês 2: ")))
    vendas_mes2.append(linha)

# Calcular o bimestre
bimestre = [[vendas_mes1[i][j] + vendas_mes2[i][j] for j in range(3)] for i in range(5)]

# Calcular as vendas de cada produto, em cada loja, no bimestre
print("Vendas de cada produto, em cada loja, no bimestre:")
for i in range(5):
    for j in range(3):
        print(f"Produto {i+1} na loja {j+1}: {bimestre[i][j]}")

# Calcular a maior venda do bimestre
maior_venda = max(max(linha) for linha in bimestre)
print(f"\nMaior venda do bimestre: {maior_venda}")

# Calcular o total vendido, por loja, no bimestre
total_loja = [sum(linha) for linha in zip(*bimestre)]
print("\nTotal vendido, por loja, no bimestre:")
for i in range(3):
    print(f"Loja {i+1}: {total_loja[i]}")

# Calcular o total vendido de cada produto no bimestre
total_produto = [sum(linha) for linha in bimestre]
print("\nTotal vendido de cada produto no bimestre:")
for i in range(5):
    print(f"Produto {i+1}: {total_produto[i]}")