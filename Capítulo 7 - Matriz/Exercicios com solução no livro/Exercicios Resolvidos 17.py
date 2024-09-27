# Faça um programa que utilize uma matriz 5 x 5 a qual aceite três tipos de valores: múltiplos de 5, múltiplos de 11 e múltiplos de 13. Devem ser lidos apenas valores maiores que zero. Após a leitura, os números devem ser distribuídos da seguinte maneira: ■ os múltiplos de 5 devem ocupar a diagonal principal; ■ os múltiplos de 11 devem ficar acima da diagonal principal; ■ os múltiplos de 13 devem ficar abaixo da diagonal principal. Como alguns números podem ser múltiplos de 5, de 11 e também de 13 (por exemplo, 55 é múltiplo de 5 e de 11; 65 é múltiplo de 5 e de 13), deve-se, primeiro, verificar se o número digitado é múltiplo de 5. Caso não seja, deve-se verificar se é múltiplo de 11. Caso não seja, deve-se verificar se é múltiplo de 13. Caso não seja, o programa deverá mostrar a mensagem Número inválido (por exemplo, o número 55 deverá ser considerado múltiplo de 5, pois esta é a comparação que será feita primeiro). Esse programa deverá observar as seguintes situações: ■ quando o usuário digitar um múltiplo de 5 e não houver mais espaço na diagonal principal, deverá mostrar a mensagem Diagonal totalmente preenchida; ■ quando o usuário digitar um múltiplo de 11 e não houver mais espaço disponível na matriz, deverá mostrar a mensagem Não existe espaço acima da diagonal principal; ■ quando o usuário digitar um múltiplo de 13 e não houver mais espaço disponível na matriz, deverá mostrar a mensagem Não existe espaço abaixo da diagonal principal; ■ quando a matriz estiver totalmente preenchida, deverá mostrar todos os elementos da matriz, junto com suas posições (linha e coluna).

# Inicializar a matriz 5 x 5 com zeros
matriz = [[0 for _ in range(5)] for _ in range(5)]

# Inicializar as variáveis para controlar o preenchimento da matriz
diagonal_preenchida = False
acima_diagonal_preenchida = False
abaixo_diagonal_preenchida = False

# Loop para preencher a matriz
while True:
    # Ler o número do usuário
    numero = int(input("Digite um número: "))

    # Verificar se o número é múltiplo de 5
    if numero % 5 == 0:
        # Verificar se a diagonal principal está preenchida
        if diagonal_preenchida:
            print("Diagonal totalmente preenchida")
        else:
            # Preencher a diagonal principal
            for i in range(5):
                if matriz[i][i] == 0:
                    matriz[i][i] = numero
                    break
            else:
                diagonal_preenchida = True

    # Verificar se o número é múltiplo de 11
    elif numero % 11 == 0:
        # Verificar se a matriz está preenchida acima da diagonal principal
        if acima_diagonal_preenchida:
            print("Não existe espaço acima da diagonal principal")
        else:
            # Preencher a matriz acima da diagonal principal
            for i in range(5):
                for j in range(i+1, 5):
                    if matriz[i][j] == 0:
                        matriz[i][j] = numero
                        break
                else:
                    continue
                break
            else:
                acima_diagonal_preenchida = True

    # Verificar se o número é múltiplo de 13
    elif numero % 13 == 0:
        # Verificar se a matriz está preenchida abaixo da diagonal principal
        if abaixo_diagonal_preenchida:
            print("Não existe espaço abaixo da diagonal principal")
        else:
            # Preencher a matriz abaixo da diagonal principal
            for i in range(5):
                for j in range(i):
                    if matriz[i][j] == 0:
                        matriz[i][j] = numero
                        break
                else:
                    continue
                break
            else:
                abaixo_diagonal_preenchida = True

    # Verificar se o número é inválido
    else:
        print("Número inválido")

    # Verificar se a matriz está totalmente preenchida
    if all(all(x != 0 for x in linha) for linha in matriz):
        print("Matriz totalmente preenchida")
        for i in range(5):
            for j in range(5):
                print(f"Elemento [{i}][{j}]: {matriz[i][j]}")
        break