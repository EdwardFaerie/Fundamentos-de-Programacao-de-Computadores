# Faça um programa que receba o total das vendas de cada vendedor de uma loja e armazene-as em um vetor. Receba também o percentual de comissão a que cada vendedor tem direito e armazene-os em outro vetor. Receba os nomes desses vendedores e armazene-os em um terceiro vetor. Existem apenas dez vendedores na loja. Calcule e mostre: um relatório com os nomes dos vendedores e os valores a receber referentes à comissão; ■ o total das vendas de todos os vendedores; ■ o maior valor a receber e o nome de quem o receberá; ■ o menor valor a receber e o nome de quem o receberá.

# Criar três vetores vazios
vendedores = [] 
vendas = [] 
comissoes = [] 

# Para um indice de 0 a 10
for i in range(0,10):
    # Digite o nome do vendedor e adicionar no vetor
    nome = input(f"Digite o nome do vendedor {i+1}: ")
    vendedores.append(nome)
    # Pode ser feito:
    # vendedores.append(input(f"Digite o nome do vendedor {i+1}: "))
    
    # Digite o total de vendas do vendedor e adicionar no vetor
    venda = float(input(f"Digite o total de vendas do vendedor {nome}: "))
    vendas.append(venda)
    # Pode ser feito:
    # vendas.append(float(input(f"Digite o total de vendas do vendedor {nome}: ")))

    # Digite o percentual de comissão do vendedor e adicionar no vetor o valor dividido por 100
    comissao = float(input(f"Digite o percentual de comissão do vendedor {nome} (%): "))
    comissoes.append(comissao / 100)
    # Pode ser feito:
    # comissoes.append(float(input(f"Digite o percentual de comissão do vendedor {vendedores[i]} (%): ")) / 100)


valores_a_receber = [venda * comissao for venda, comissao in zip(vendas, comissoes)]

# Pode ser feito:
# valores_a_receber = []
# for i in range(10):
#     valor_a_receber = vendas[i] * comissoes[i]
#     valores_a_receber.append(valor_a_receber)

# A função zip é uma função built-in do Python que permite iterar sobre múltiplos iteráveis (como listas, tuplas, etc.) em paralelo. Ela "zipa" os elementos de cada iterável em pares, criando um iterador que retorna esses pares.

# Mostrar o relatório de comissões
print("Relatório de comissões:")
# para cada indice, nome e valor nos dois vetores "zipados": vendedores e valores_a_receber mostrar indice, nome e valor de comissão em até duas casas decimais.  
for i, (nome, valor) in enumerate(zip(vendedores, valores_a_receber)):
    print(f"{i+1}. {nome}: R$ {valor:.2f}")
# Pode ser feito:
# contador = 1
# for nome in vendedores:
#     valor = valores_a_receber[contador - 1]
#     print(f"{contador}. {nome}: R$ {valor:.2f}")
#     contador += 1

# Somar todas as vendas e mostrar o valor total della em até duas casas decimais
total_vendas = sum(vendas)
print(f"\nTotal de vendas: R$ {total_vendas:.2f}")

# Encontrar o maior valor a receber
maior_valor = max(valores_a_receber)

# Encontrar o menor valor a receber
menor_valor = min(valores_a_receber)

# Encontrar o valor do indice do maior valor
indice_maior = valores_a_receber.index(maior_valor)

# Encontrar o valor do indice do menor valor
indice_menor = valores_a_receber.index(menor_valor)

# Mostrar o maior valor a receber e o nome do vendedor
print(f"\nMaior valor a receber: R$ {maior_valor:.2f} ({vendedores[indice_maior]})")

# Mostrar o menor valor a receber e o nome do vendedor
print(f"Menor valor a receber: R$ {menor_valor:.2f} ({vendedores[indice_menor]})")