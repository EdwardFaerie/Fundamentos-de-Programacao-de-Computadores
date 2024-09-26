# Faça um programa que preencha um vetor com os nomes de sete alunos e carregue outro vetor com a média final desses alunos. Calcule e mostre: ■ o nome do aluno com maior média (desconsiderar empates); ■ para cada aluno não aprovado, isto é, com média menor que 7, mostrar quanto esse aluno precisa tirar na prova de exame final para ser aprovado. Considerar que a média para aprovação no exame é 5.

# Cria listas vazias para armazenar os nomes e médias dos alunos
nomes = []
medias = []

# Loop que irá rodar 7 vezes para solicitar informações de 7 alunos
for i in range(7):
    # Solicita o nome do aluno e o adiciona à lista de nomes
    nomes.append(input("Digite o nome do aluno {}: ".format(i+1)))
    # Solicita a média final do aluno e a adiciona à lista de médias
    medias.append(float(input("Digite a média final do aluno {}: ".format(i+1))))

# Encontra a maior média e o aluno correspondente
maior_media = max(medias)
aluno_maior_media = nomes[medias.index(maior_media)]

# Imprime o aluno com a maior média
print("Aluno com maior média:", aluno_maior_media)

# Loop que irá percorrer as médias dos alunos
for i in range(7):
    # Verifica se a média do aluno é menor que 7
    if medias[i] < 7:
        # Calcula a nota necessária para aprovação no exame
        nota_exame = 5 - (medias[i] - 5)
        # Imprime a mensagem com a nota necessária para aprovação
        print("O aluno {} precisa tirar {:.2f} no exame para ser aprovado.".format(nomes[i], nota_exame))