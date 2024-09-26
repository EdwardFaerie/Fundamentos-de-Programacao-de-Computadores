# Faça um programa para controlar o estoque de mercadorias de uma empresa. inicialmente o programa deverá preencher dois vetores com dez posições cada, onde o primeiro corresponde ao código do produto e o segundo o total desse produto em estoque. Logo após, o programa deverá um conjunto inderteminado de dados contendo o código de um cliente e o código do produto que ele deseja comprar, juntamente com a quantidade. Código do cliente igual a zero indica fim do programa. O Programa deverá verificar: Se o código de produto solicitado existe, se existir tentar atender ao pedido caso contrário informar a mensagem código não existente. Cada pedido feito por um cliente só pode ser atendido integralmente. Caso isso não seja possivel escrever a mensagem: Não temos estoque suficiente dessa mercadoria, caso possa atender escreava a mensagem: Pedido atendido. Obrigado e volte sempre. Efetuar a atualização do estoque se o pedido for atendido integralmente. No final do programa escrever os códigos dos produtos e seus respectivos estoques.

# Criar dois vetores vazios de 10 indices que tem valor zero
codigos_produtos = [0] * 10
estoques = [0] * 10

# Para cada indice do vetor de produtos, atribuir um valor de 1 a 10
for i in range(10):
    codigos_produtos[i] = int(input(f"Código do produto {i+1}: "))
    estoques[i] = int(input(f"Estoque do produto {i+1}: "))

# Enquanto o código executar fazer loop
while True:
    # Perguntar o código do cliente
    codigo_cliente = int(input("Código do cliente (0 para sair): "))
    if codigo_cliente == 0: # Se o código do cliente for zero então:
        break # Finalizar loop 
    # Perguntar o código do produto e a quantidade
    codigo_produto = int(input("Código do produto: "))
    quantidade = int(input("Quantidade desejada: "))
    
    # Se o código do produto estar no vetor de códigos de produtos então
    if codigo_produto in codigos_produtos:
        # Ver qual o indice do produto selecionado
        indice_produto = codigos_produtos.index(codigo_produto)
        # Se a quantidade desejada for menor ou igual ao estoque então
        if estoques[indice_produto] >= quantidade:
            estoques[indice_produto] -= quantidade # É retirado do estoque a quantidade pedida
            print("Pedido atendido. Obrigado e volte sempre.") # Mostrar ao usuário
        else:
            print("Não temos estoque suficiente dessa mercadoria.") # Não há estoque então mostrar ao usuário que não tem o suficiente da mercadoria
    else:
        print("Código não existente.") # Código inexistente

# Estoques finais
print("Estoques finais:")
for i in range(10): # Para indice de 0 a 10 mostrar código do produto com as unidades
    print(f"Código {codigos_produtos[i]}: {estoques[i]} unidades")