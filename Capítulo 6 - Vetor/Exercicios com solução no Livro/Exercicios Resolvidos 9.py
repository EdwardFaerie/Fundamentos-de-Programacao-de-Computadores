# Faça um programa de reserva de passagens aéreas, ele deve ler as informações sobre os voos (numero, origem e destino) e o numero de lugares disponiveis para doze aviões (um vetor para cada um desses dados) depois da leitura deve elecionar entre um menu, consultar, efetuar reserva ou sair. Quando a opção for escolida for a consultar deve ser disponibilizado mais um menu com as seguintes opções: Por número de voo, por origem e por destino; Quando a opção for escolida for efetuar reserva deverá perguntar o número do voo em que deseja viajar, assim o programa deve entregar as seguintes respostas: Reserva confirmada, voo lotado ou voo inexistente; Após cada operação deve ter uma opção de Sair.

# Lista de voos com informações sobre cada voo
voos = [
    ['Avião 1', 1, 'Jales - São Paulo', 'Paris - França', 'Não reservado'],
    ['Avião 2', 2, 'Paris - França', 'Jales - São Paulo', 'Reservado'],
]

# Variável para controlar o loop do menu
sair = False

# Loop do menu
while sair != True:
    # Imprime o menu principal
    print("Menu principal:")
    print("1 - Consultar voos")
    print("2 - Efetuar reserva")
    print("3 - Sair")
    
    # Lê a opção do usuário
    opcao = int(input("Escolha uma opção: "))

    # Verifica se a opção é válida
    if type(opcao) != int:
        opcao  = int(input("Opção inválida, por favor escolha uma opção válida:"))
        break       
    elif opcao > 3:
        opcao  = int(input("Opção inválida, por favor escolha uma opção válida:"))
    elif opcao < 1:
        opcao = int(input("Opção inválida, por favor escolha uma opção válida:"))

    # Opção 1: Consultar voos
    elif opcao == 1:
        # Imprime o menu de consulta
        print("Menu de consulta:")
        print("1 - Por número de voo")
        print("2 - Por origem")
        print("3 - Por destino")
        
        # Lê a opção de consulta
        opcao2 = int(input("Escolha uma opção: "))
        
        # Verifica se a opção de consulta é válida
        if type(opcao2) != int:
            opcao2 = int(input("Opção inválida, por favor escolha uma opção:"))
        elif opcao2 > 3:
            opcao2 = int(input("Opção inválida, por favor escolha uma opção:"))
        elif opcao2 < 1:
            opcao2 = int(input("Opção inválida, por favor escolha uma opção:"))
        
        # Consulta por número de voo
        elif opcao2 == 1:
            num_voo = int(input("Digite o número do voo: "))
            for i in range(len(voos)):
                if voos[i][1] == num_voo:
                    print(f"Voo {num_voo} encontrado:")
                    print(f"{voos[i]}")
        
        # Consulta por origem
        elif opcao2 == 2:
            origem = input("Digite a origem: ")
            for i in range(len(voos)):
                if origem in voos[i][2]:
                    print(f"Voo encontrado:")
                    print(f"{voos[i]}")
        
        # Consulta por destino
        elif opcao2 == 3:
            destino = input("Digite o destino: ")
            for i in range(len(voos)):
                if destino in voos[i][3]:
                    print(f"Voo encontrado:")
                    print(f"{voos[i]}")

    # Opção 2: Efetuar reserva
    elif opcao == 2:
        # Imprime o menu de reserva
        print("Menu de reserva:")
        print("1 - Por número de voo")
        print("2 - Por origem")
        print("3 - Por destino")
        
        # Lê a opção de reserva
        opcao2 = int(input("Escolha uma opção: "))
        
        # Verifica se a opção de reserva é válida
        if type(opcao2) != int:
            opcao2 = int(input("Opção inválida, por favor escolha uma opção:"))
        elif opcao2 > 3:
            opcao2 = int(input("Opção inválida, por favor escolha uma opção:"))
        elif opcao2 < 1:
            opcao2 = int(input("Opção inválida, por favor escolha uma opção:"))
        
        # Reserva por número de voo
        elif opcao2 == 1:
            num_voo = int(input("Digite o número do voo: "))
            for i in range(len(voos)):
                if voos[i][1] == num_voo:
                    print(f"Voo {num_voo} encontrado:")
                    print(f"{voos[i]}")
                    if voos[i][4] == 'Reservado':
                        print("Voo já está reservado por outra pessoa!")
                    else:
                        reserva = input ("Deseja reservar o voo? (s/n): ")
                        if reserva.lower() == "s":
                            voos[i][4] = "Reservado"
                            print(f"Voo {num_voo} reservado com sucesso!")
                        else:
                            print(f"Voo {num_voo} não reservado!")
                else:
                    print(f"Voo não encontrado!")
        
        # Reserva por origem
        elif opcao2 == 2:
            origem = input("Digite a origem: ")
            for i in range(len(voos)):
                if origem in voos[i][2]:
                    print(f"Voo encontrado:")
                    print(f"{voos[i]}")
                    if voos[i][4] == 'Reservado':
                        print("Voo já está reservado por outra pessoa!")
                    else:
                        reserva = input("Deseja reservar o voo? (s/n): ")
                        if reserva.lower() == "s":
                            voos[i][4] = "Reservado"
                            print(f"Voo {voos[i][1]} reservado com sucesso!")
                        else:
                            print(f"Voo {voos[i][1]} não reservado!")
        
        # Reserva por destino
        elif opcao2 == 3:
            destino = input("Digite o destino: ")
            for i in range(len(voos)):
                if destino in voos[i][3]:
                    print(f"Voo encontrado:")
                    print(f"{voos[i]}")
                    if voos[i][4] == 'Reservado':
                        print("Voo já está reservado por outra pessoa!")
                    else:
                        reserva = input("Deseja reservar o voo? (s/n): ")
                        if reserva.lower() == "s":
                            voos[i][4] = "Reservado"
                            print(f"Voo {voos[i][1]} reservado com sucesso!")
                        else:
                            print(f"Voo {voos[i][1]} não reservado!")

    # Opção 3: Sair
    elif opcao == 3:
        print("Sair do sistema...")
        sair = True