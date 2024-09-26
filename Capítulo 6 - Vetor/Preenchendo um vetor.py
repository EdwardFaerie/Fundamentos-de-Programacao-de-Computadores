# Crie um programa que tenha a entrada de 5 valores inteiros e adicione eles a uma lista e no final mostre a lista

lista = [] # Criar uma lista vazia
for indice in range(0,5): # Verificar indice em um valor entre 0 e 5
    lista.append(int(input(f"Digite o {indice} com Número: "))) # Inserir um novo valor na lista sendo digitado pelo usuário
print(lista) # Mostrar a lista por completo