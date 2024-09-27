# Faça um programa que utilize uma matriz com dimensões máximas de cinco linhas e quatro colunas. Solicite que sejam digitados os números que serão armazenados na matriz da seguinte maneira: ■ se o número digitado for par, deve ser armazenado em uma linha de índice par; ■ se o número digitado for ímpar, deve ser armazenado em uma linha de índice ímpar; ■ as linhas devem ser preenchidas de cima para baixo (por exemplo, os números pares digitados devem ser armazenados inicialmente na primeira linha par; quando essa linha estiver totalmente preenchida, deve ser utilizada a segunda linha par e assim sucessivamente; o mesmo procedimento deve ser adotado para os números ímpares); ■ quando não couberem mais números pares ou ímpares, o programa deverá mostrar uma mensagem ao usuário; ■ quando a matriz estiver totalmente preenchida, o programa deverá encerrar a leitura dos números e mostrar todos os elementos armazenados na matriz.

# Inicializar a matriz com dimensões máximas de cinco linhas e quatro colunas
matriz = [[0 for _ in range(4)] for _ in range(5)]

# Inicializar as variáveis para controlar o preenchimento da matriz
linha_par = 0
linha_impar = 1

# Loop para preencher a matriz
while True:
    # Ler o número do usuário
    numero = int(input("Digite um número: "))

    # Verificar se o número é par
    if numero % 2 == 0:
        # Verificar se a linha par está preenchida
        if linha_par >= 5 or matriz[linha_par].count(0) == 0:
            print("Não couberam mais números pares.")
            break
        # Preencher a linha par
        for j in range(4):
            if matriz[linha_par][j] == 0:
                matriz[linha_par][j] = numero
                break
        # Avançar para a próxima linha par
        linha_par += 2

    # Verificar se o número é ímpar
    else:
        # Verificar se a linha ímpar está preenchida
        if linha_impar >= 5 or matriz[linha_impar].count(0) == 0:
            print("Não couberam mais números ímpares.")
            break
        # Preencher a linha ímpar
        for j in range(4):
            if matriz[linha_impar][j] == 0:
                matriz[linha_impar][j] = numero
                break
        # Avançar para a próxima linha ímpar
        linha_impar += 2

    # Verificar se a matriz está totalmente preenchida
    if all(all(x != 0 for x in linha) for linha in matriz):
        print("Matriz totalmente preenchida.")
        break

# Mostrar a matriz
print("Matriz:")
for linha in matriz:
    print(linha)