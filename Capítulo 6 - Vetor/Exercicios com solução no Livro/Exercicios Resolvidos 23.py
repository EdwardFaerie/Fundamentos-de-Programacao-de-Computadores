# Uma empresa possui ônibus com 48 lugares (24 nas janelas e 24 no corredor). Faça um programa que utilize dois vetores para controlar as poltronas ocupadas no corredor a na janela. Considere que 0nrepresenta poltrona desocupada e 1 ocupada. Inicialmente todas as poltronas estarão livres, Depois disso o programa deverá apresentar as seguintes opções: Vender passagem; mostrar mapa de ocupação do ônibus; encerrar. Quando a opção for vender passagem deverá ser perguntado se o usuário deseja janela ou corredor e o número da poltrona. O programa deverá então dar uma das seguintes mensagens: Venda efetivada (se a poltrona estiver livre marcando-a como ocupada); Poltrona ocupada (se a poltrona não estiver disponivel para venda); Onibus lotado (quando todas as poltronas estiverem ocupadas); Quando a opção for mostrar mapa de ocupação deverá mostrar uma lista com o número da poltrona da janela e do corredor com a situação da poltrona sendo ocupada ou livre.

# Listas vazias para armazenar a ocupação das poltronas do ônibus
corridor_seats = [0] * 24
window_seats = [0] * 24

# Função para mostrar o mapa de ocupação do ônibus
def show_seat_map():
    print("Mapa de ocupação do ônibus:")
    for i in range(24):
        # Verifica se a poltrona da janela está ocupada
        print(f"Janela {i+1}: {'Ocupada' if window_seats[i] == 1 else 'Livre'}")
        # Verifica se a poltrona do corredor está ocupada
        print(f"Corredor {i+1}: {'Ocupada' if corridor_seats[i] == 1 else 'Livre'}")
    print()

# Função para vender passagens
def sell_ticket():
    # Pede ao usuário que escolha o tipo de poltrona
    seat_type = input("Deseja janela ou corredor? ")
    # Pede ao usuário que digite o número da poltrona
    seat_number = int(input("Número da poltrona: ")) - 1
    
    # Verifica se a poltrona da janela está disponível
    if seat_type == "janela":
        if window_seats[seat_number] == 0:
            # Vende a passagem e marca a poltrona como ocupada
            window_seats[seat_number] = 1
            print("Venda efetivada!")
        else:
            print("Poltrona ocupada!")
    # Verifica se a poltrona do corredor está disponível
    elif seat_type == "corredor":
        if corridor_seats[seat_number] == 0:
            # Vende a passagem e marca a poltrona como ocupada
            corridor_seats[seat_number] = 1
            print("Venda efetivada!")
        else:
            print("Poltrona ocupada!")
    else:
        print("Opção inválida!")

# Função para verificar se o ônibus está lotado
def is_bus_full():
    # Verifica se todas as poltronas estão ocupadas
    return all(seat == 1 for seat in corridor_seats + window_seats)

# Loop principal do programa
while True:
    print("Opções:")
    print("1. Vender passagem")
    print("2. Mostrar mapa de ocupação do ônibus")
    print("3. Encerrar")
    # Pede ao usuário que escolha uma opção
    option = input("Escolha uma opção: ")
    
    # Verifica a opção escolhida
    if option == "1":
        # Vende uma passagem
        sell_ticket()
        # Verifica se o ônibus está lotado
        if is_bus_full():
            print("Ônibus lotado!")
    elif option == "2":
        # Mostra o mapa de ocupação do ônibus
        show_seat_map()
    elif option == "3":
        # Encerra o programa
        break
    else:
        print("Opção inválida!")

# Observação: O código utiliza listas para armazenar a ocupação das poltronas do ônibus e funções para realizar operações como vender passagens e mostrar o mapa de ocupação. O loop principal do programa é utilizado para controlar a execução do programa e chamar as funções correspondentes às opções escolhidas pelo usuário.