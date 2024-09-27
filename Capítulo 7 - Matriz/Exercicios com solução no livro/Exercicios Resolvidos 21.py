# Crie um programa que utilize uma matriz com as dimensões fornecidas pelo usuário e execute as solicitações a seguir. Para realizar essa tarefa, a matriz deverá ser obrigatoriamente quadrada (número igual de linhas e colunas). Sendo assim, solicite que seja informada a dimensão da matriz. Posteriormente, o programa deverá realizar a leitura dos elementos que vão compor a matriz. Por fim, deverá somar e mostrar os elementos que estão abaixo da diagonal secundária.

# Solicitar a dimensão da matriz
dimensao = int(input("Digite a dimensão da matriz (número de linhas e colunas): "))

# Verificar se a dimensão é válida
if dimensao <= 0:
    print("Dimensão inválida. Por favor, digite um número positivo.")
else:
    # Inicializar a matriz
    matriz = [[0 for _ in range(dimensao)] for _ in range(dimensao)]

    # Ler os elementos da matriz
    for i in range(dimensao):
        for j in range(dimensao):
            matriz[i][j] = int(input(f"Digite o elemento [{i+1}][{j+1}]: "))

    # Somar os elementos abaixo da diagonal secundária
    soma = 0
    for i in range(dimensao):
        for j in range(dimensao):
            if i + j >= dimensao - 1:
                soma += matriz[i][j]

    # Mostrar a soma dos elementos abaixo da diagonal secundária
    print("Soma dos elementos abaixo da diagonal secundária:", soma)