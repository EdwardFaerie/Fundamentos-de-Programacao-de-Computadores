# Faça um programa que preencha 3 vetores com cinco posições cada. o primeiro vetor receberá os nomes de cinco funcionários; o segundo e o terceiro vetor receberão, respectivamente, o salário e tempo de serviço de cada um. Mostre um primeiro relatório apenas com os nomes dos funcionários que não terão aumento; mostre um segundo relatório apenas com os nomes e os novos salários dos funcionários que terão aumento. Sabe se que só terão aumento quando possuem tempo de serviço maior que cinco anos e salário inferior a R$ 800,00, caso as duas condições forem satisfeitas o funcionário terá 35% de aumento no salário, caso a condição satisfeita seja somente de condição de tempo o aumento será de 25%, caso a condição satisfeita seja somente a de salario ele terá 15% de aumento.

# Listas vazias para armazenar os nomes, salários e tempos de serviço dos funcionários
nomes = [input("Informe o nome do funcionário {}: ".format(i+1)) for i in range(5)]
salarios = [float(input("Informe o salário do funcionário {}: R$ ".format(i+1))) for i in range(5)]
tempos_servico = [int(input("Informe o tempo de serviço do funcionário {}: ".format(i+1))) for i in range(5)]

# Listas vazias para armazenar os funcionários sem aumento e com aumento
funcionarios_sem_aumento = []
funcionarios_com_aumento = []

# Loop para calcular o aumento de salário de cada funcionário
for i in range(5):
    # Verifica se o funcionário tem mais de 5 anos de serviço e salário inferior a R$ 800
    if tempos_servico[i] > 5 and salarios[i] < 800:
        # Se sim, calcula o aumento de 35%
        aumento = salarios[i] * 0.35
    # Verifica se o funcionário tem mais de 5 anos de serviço e salário superior a R$ 800
    elif tempos_servico[i] > 5 and salarios[i] > 800:
        # Se sim, calcula o aumento de 25%
        aumento = salarios[i] * 0.25
    # Verifica se o salário do funcionário é inferior a R$ 800 e o tempo de serviço é superior a 5 anos
    elif salarios[i] < 800 and tempos_servico[i] > 5:
        # Se sim, calcula o aumento de 15%
        aumento = salarios[i] * 0.15
    else:
        # Se não, adiciona o funcionário à lista de funcionários sem aumento
        funcionarios_sem_aumento.append(nomes[i])
        continue
    
    # Calcula o novo salário do funcionário
    novo_salario = salarios[i] + aumento
    # Adiciona o funcionário à lista de funcionários com aumento
    funcionarios_com_aumento.append((nomes[i], novo_salario))

# Imprime o relatório de funcionários sem aumento
print("Relatório 1: Funcionários sem aumento")
for funcionario in funcionarios_sem_aumento:
    print(funcionario)

# Imprime o relatório de funcionários com aumento
print("\nRelatório 2: Funcionários com aumento")
for funcionario, novo_salario in funcionarios_com_aumento:
    print("{}: R$ {:.2f}".format(funcionario, novo_salario))