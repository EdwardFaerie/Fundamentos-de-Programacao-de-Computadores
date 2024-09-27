# Crie um programa que receba as vendas semanais (de um mês) de cinco vendedores de uma loja e armazene essas vendas em uma matriz. O programa deverá calcular e mostrar: ■ o total de vendas do mês de cada vendedor; ■ o total de vendas de cada semana (todos os vendedores juntos); ■ o total de vendas do mês.

# Receber as vendas semanais de cinco vendedores
vendas = []
for i in range(5):
    linha = []
    for j in range(4):
        linha.append(int(input(f"Digite as vendas do vendedor {i+1} na semana {j+1}: ")))
    vendas.append(linha)

# Calcular o total de vendas do mês de cada vendedor
total_vendas_vendedor = [sum(linha) for linha in vendas]

# Calcular o total de vendas de cada semana (todos os vendedores juntos)
total_vendas_semana = [sum(coluna) for coluna in zip(*vendas)]

# Calcular o total de vendas do mês
total_vendas_mes = sum(total_vendas_vendedor)

# Mostrar os resultados
print("Total de vendas do mês de cada vendedor:", total_vendas_vendedor)
print("Total de vendas de cada semana (todos os vendedores juntos):", total_vendas_semana)
print("Total de vendas do mês:", total_vendas_mes)