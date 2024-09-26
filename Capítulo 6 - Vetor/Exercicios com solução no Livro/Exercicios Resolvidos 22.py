# Faça um programa que simule o controle bancário. Para tanto, devem ser lidos os código de dez contas e seus respectivos saldos. Os códigos devem ser armazenados em um vetor de números inteiros (Não pode haver mais de uma conta com mesmo código) e os saldos devem ser armazenados em um vetor de números reais. O saldo deverá ser cadastrado na mesma posição do código. Depois de fazer a leitura dos valores deverá aparecer o seguinte menu na tela: 1. Efetuar depósito 2. Efetuar Saque 3. Consultar o ativo banco (somatório de todos os saldos de toos os clientes.) 4. Finalizar o programa; Para efetuar o depósito deve-se solicitar código da conta e valor a ser depositado. Se a conta não estiver cadastrada deverá aparecer uma mensagem de conta não encontrada e voltar ao menu caso encontre a conta, atualizar o saldo; Para efetuar o  saque deve-se solicitar código da conta e valor a ser sacado. Se a conta não não estiver cadastrada, deverá mostrar a mensagem conta não encontrada e voltar ao me u, caso a conta existirm verificar se seu saldo é suficiente para realizar o saque e voltar ao menu, caso contrario aparecer a mensagem saldo não suficiente. Para consultar o ativo bancario deve se somar todas as contas do banco e depois motrar este valor, voltar ao menu.

# Listas vazias para armazenar os códigos de conta e saldos
CodigoContas = []
Saldos = []

# Loop para criar 10 contas bancárias
for i in range(10):
    # Pede ao usuário que digite o código da conta
    code = int(input("Código de conta: "))
    # Verifica se o código da conta já existe
    while code in CodigoContas:
        print("Código da Conta já existe coloque outro código")
        code = int(input("Código de conta: "))
    # Adiciona o código da conta à lista
    CodigoContas.append(code)
    # Pede ao usuário que digite o saldo inicial
    balance = float(input("Saldo Inicial: "))
    # Adiciona o saldo inicial à lista
    Saldos.append(balance)

# Função para realizar depósitos
def deposit():
    # Pede ao usuário que digite o código da conta
    code = int(input("Código da conta: "))
    # Verifica se a conta existe
    if code not in CodigoContas:
        print("Conta não encontrada.")
        return
    # Encontra o índice da conta
    index = CodigoContas.index(code)
    # Pede ao usuário que digite o valor do depósito
    amount = float(input("Depósito: "))
    # Realiza o depósito
    Saldos[index] += amount
    print("Depositado com sucesso.")

# Função para realizar saques
def withdrawal():
    # Pede ao usuário que digite o código da conta
    code = int(input("Código da conta: "))
    # Verifica se a conta existe
    if code not in CodigoContas:
        print("Conta não encontrada.")
        return
    # Encontra o índice da conta
    index = CodigoContas.index(code)
    # Pede ao usuário que digite o valor do saque
    amount = float(input("Saque: "))
    # Verifica se o saldo é suficiente
    if Saldos[index] < amount:
        print("Saldo não suficiente.")
        return
    # Realiza o saque
    Saldos[index] -= amount
    print("Saque com sucesso.")

# Função para consultar o saldo total do banco
def check_balance():
    # Calcula o saldo total do banco
    total_balance = sum(Saldos)
    print("Saldo total: ", total_balance)

# Variável para controlar o loop do menu principal
Sair = False

# Loop do menu principal
while Sair != True:
    # Imprime o menu principal
    print("\nMenu Principal:")
    print("1. Efetuar depósito")
    print("2. Efetuar Saque")
    print("3. Consultar o ativo banco")
    print("4. Finalizar o programa")
    # Pede ao usuário que digite a opção desejada
    opcao = int(input("Digite a opção desejada: "))
    print("\n")

    # Verifica se a opção é válida
    if type(opcao) != int:
        print("Opção inválida. Por favor, digite um número inteiro.")
        break
    elif opcao > 4:
        print("Opção inválida. Por favor, digite um número entre 1 e 4")
    elif opcao < 1:
        print("Opção inválida. Por favor, digite um número entre 1 e 4")
    # Chama a função correspondente à opção escolhida
    elif opcao == 1:
        deposit()
    elif opcao == 2:
        withdrawal()
    elif opcao == 3:
        check_balance()
    elif opcao == 4:
        print(f"Finalizando Programa")
        break

# Observação: O código utiliza um loop para criar 10 contas bancárias e armazenar os códigos de conta e saldos em listas. As funções deposit, withdrawal e check_balance são utilizadas para realizar depósitos, saques e consultar o saldo total do banco, respectivamente. O loop do menu principal é utilizado para controlar a execução do programa e chamar as funções correspondentes às opções escolhidas pelo usuário.