# faça um programa que preencha um vetor com os modelos de cinco carros, outro vetor com consumo destes carros. Calcule e mostre: o modelo de carro mais ecônomico e quantos litros de combustível cada um dos carros cadastrados consome para percorrer 1.000 km.

# Listas vazias para armazenar os modelos de carros e seus consumos
carros = []
consumo = []

# Loop para preencher as listas de carros e consumos
for i in range(5):
    # Pede ao usuário que digite o modelo do carro atual
    modelo = input("Digite o modelo do carro {}: ".format(i+1))
    # Adiciona o modelo ao final da lista de carros
    carros.append(modelo)
    
    # Pede ao usuário que digite o consumo do carro atual (litros/km)
    litros_por_km = float(input("Digite o consumo do carro {} (litros/km): ".format(i+1)))
    # Adiciona o consumo ao final da lista de consumos
    consumo.append(litros_por_km)

# Encontra o menor consumo na lista de consumos
menor_consumo = min(consumo)
# Encontra o índice do menor consumo na lista de consumos
indice_menor_consumo = consumo.index(menor_consumo)
# Encontra o modelo do carro mais econômico (aquele com o menor consumo)
modelo_mais_economico = carros[indice_menor_consumo]

# Imprime o modelo do carro mais econômico
print("O modelo de carro mais econômico é o {}.".format(modelo_mais_economico))
# Imprime o consumo por 1.000 km de cada carro
print("Consumo por 1.000 km:")
for i in range(5):
    # Imprime o modelo do carro e seu consumo por 1.000 km (arredondado para 2 casas decimais)
    print("{}: {:.2f} litros".format(carros[i], consumo[i] * 1000))