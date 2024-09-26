# Faça um programa que preenche um vetor de 15 números inteiros e verifique a existência de elemento igual a 30, mostrando a posição em que aparecem

# 15 valores iguais a 0 dentro do vetor 
vetor = [0] * 15

# Importa a biblioteca "random"
import random

# Para um indice de 0 a 15
for i in range(15):
    # O vetor de indice 0 a 15 será atribuido um valor aleatório de 1 entre 50
    vetor[i] = random.randint(1, 50)

# Verificar se existe o valor 30 no vetor
posicoes = [i for i, x in enumerate(vetor) if x == 30]

# Pode ser feito também da seguinte forma:
# posicoes = []
# if 30 in vetor:
#     posicoes.append(vetor.index(30))

# Se o vetor posicoes tem algum valor então mostrar posição do elemento 30
if posicoes:
    print("O elemento 30 aparece nas posições:", posicoes)
else: # Caso não tenha nenhum número 30 no vetor então mostrar que não foi encontrado
    print("O elemento 30 não foi encontrado no vetor.")