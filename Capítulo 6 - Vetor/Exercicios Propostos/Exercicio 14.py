# Faça um programa que receba o nome e duas notas de seis alunos e mostre o relatório a seguir. Relatório de notas: média da classe = ? ■ percentual de alunos aprovados = ?% ■ percentual de alunos de exame = ?% ■ percentual de alunos reprovados = ?%

# Criamos uma lista vazia para armazenar os alunos com suas médias
alunos = []

# Loop para coletar informações de 6 alunos
for i in range(6):
    # Pedimos o nome do aluno
    nome = input("Digite o nome do {}º aluno: ".format(i+1))
    
    # Pedimos as duas notas do aluno
    nota1 = float(input("Digite a primeira nota do {}: ".format(nome)))
    nota2 = float(input("Digite a segunda nota do {}: ".format(nome)))
    
    # Calculamos a média do aluno
    media_aluno = (nota1 + nota2) / 2
    
    # Adicionamos o aluno com sua média à lista
    alunos.append([nome, media_aluno])

# Imprimimos o relatório de notas
print("\nRelatório de notas:")

# Calculamos a média da classe
media_classe = sum([media for _, media in alunos]) / len(alunos)
print("Média da classe = {:.1f}".format(media_classe))

# Criamos listas para armazenar os alunos aprovados, de exame e reprovados
aprovados = [aluno for aluno, media in alunos if media >= 7]
exame = [aluno for aluno, media in alunos if 5 <= media < 7]
reprovados = [aluno for aluno, media in alunos if media < 5]

# Calculamos os percentuais de alunos aprovados, de exame e reprovados
percent_aprovados = (len(aprovados) / len(alunos)) * 100
percent_exame = (len(exame) / len(alunos)) * 100
percent_reprovados = (len(reprovados) / len(alunos)) * 100

# Imprimimos os percentuais
print("Percentual de alunos aprovados = {:.1f}%".format(percent_aprovados))
print("Percentual de alunos de exame = {:.1f}%".format(percent_exame))
print("Percentual de alunos reprovados = {:.1f}%".format(percent_reprovados))