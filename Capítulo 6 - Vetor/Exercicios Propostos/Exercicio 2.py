# Faça um programa que preencha um vetor com sete números inteiros, calcule e mostre: Os números multiplos de 2, os números multiplos de 3, os números multiplos de 2 e 3

# Pede ao usuário inserir numeros inteiros 7 vezes
vetor = [int(input(f"Digite o {i+1}º número: ")) for i in range(7)]

# Pode se escrever também destá forma o código acima:

# vetor = []
# for i in range(0,7):
#   vetor.append(f"DIgite o {i+1}º número: ")

# Verificar se são multiplos de 2
multiplos_de_2 = [num for num in vetor if num % 2 == 0]
print("Números multiplos de 2:", multiplos_de_2)

# Verificar se são multiplos de 3
multiplos_de_3 = [num for num in vetor if num % 3 == 0]
print("Números multiplos de 3:", multiplos_de_3)

# Verificar se são multiplos de 2 e 3
multiplos_de_2_e_3 = [num for num in vetor if num % 2 == 0 and num % 3 == 0]
print("Números multiplos de 2 e 3:", multiplos_de_2_e_3)

# se pode escrever também desta forma o código acima:
# for num in vetor:
#     if num % 2 == 0 and num % 3 == 0:
#         multiplos_de_2_e_3.append(num)
#     elif num % 2 == 0:
#         multiplos_de_2.append(num)
#     elif num % 3 == 0:
#         multiplos_de_3.append(num)
# print("Números multiplos de 2:", multiplos_de_2)
# print("Números multiplos de 3:", multiplos_de_3)
# print("Números multiplos de 2 e 3:", multiplos_de_2_e_3)
