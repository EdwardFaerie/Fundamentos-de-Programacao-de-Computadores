# Faça um programa que receba o nome de oito clientes e armazene-os em um vetor. Em um segundo vetor, armazene a quantidade de DVDs locados em 2011 por cada um dos oito clientes. Sabe-se que, para cada dez locações, o cliente tem direito a uma locação grátis. Faça um programa que mostre o nome de todos os clientes, com a quantidade de locações grátis a que ele tem direito

# Criamos listas vazias para armazenar os nomes dos clientes e suas locações
nomes_clientes = []
locacoes_clientes = []

# Loop para coletar informações de 8 clientes
for i in range(8):
    # Pedimos o nome do cliente
    nome = input("Digite o nome do {}º cliente: ".format(i+1))
    
    # Adicionamos o nome do cliente à lista
    nomes_clientes.append(nome)
    
    # Pedimos a quantidade de DVDs locados pelo cliente em 2011
    locacoes = int(input("Digite a quantidade de DVDs locados em 2011 pelo {}: ".format(nome)))
    
    # Adicionamos a quantidade de locações à lista
    locacoes_clientes.append(locacoes)

# Imprimimos o relatório de locações
print("\nRelatório de locações:")

# Loop para calcular e imprimir as locações grátis para cada cliente
for i in range(8):
    # Calculamos a quantidade de locações grátis para o cliente (1 locação grátis para cada 10 locações)
    locacoes_gratis = locacoes_clientes[i] // 10
    
    # Imprimimos o resultado
    print("{} tem direito a {} locações grátis.".format(nomes_clientes[i], locacoes_gratis))