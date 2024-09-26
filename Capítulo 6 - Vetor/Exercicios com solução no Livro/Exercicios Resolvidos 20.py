# Faça um programa que leia um vetor com 5 posições para números reais, e depois, um código inteiro. Se o código for zero finalize o programa; se for 1 mostre o vetor na ordem direta e se for 2 mostre o vetor na ordem inversa

# Lista vazia para armazenar os números reais
lista = [float(input(f"Digite um número Real para a posição {i}: ")) for i in range(0,5)]

# Pede ao usuário que digite um código para escolher a ação
codigo = int(input(f"Digite 0 para finalizar\n1 para mostrar em ordem direta\n2 para mostrar em ordem inversa\n>>"))

# Verifica o código digitado
if codigo < 0 or codigo > 2:
    # Se o código for inválido, imprime uma mensagem de erro
    print("Número Invalido, renicie o programa.")
elif codigo == 0:
    # Se o código for 0, imprime uma mensagem de finalização
    print("Finalizando programa.")
elif codigo == 1:
    # Se o código for 1, imprime a lista em ordem direta
    print(sorted(lista,reverse=False))
elif codigo == 2:
    # Se o código for 2, imprime a lista em ordem inversa
    print(sorted(lista,reverse=True))

# Observação: O código utiliza a função sorted para ordenar a lista de números reais. A função sorted retorna uma nova lista ordenada, sem modificar a lista original. O parâmetro reverse é utilizado para especificar a ordem da lista: False para ordem direta e True para ordem inversa.