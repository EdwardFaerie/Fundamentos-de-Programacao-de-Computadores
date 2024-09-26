# Faça um programa que receba o nome e a nota de oito alunos e mostre o relatório a seguir: Digite o nome do 1o aluno: Carlos Digite a nota do Carlos: 8 Digite o nome do 2o aluno: Pedro Digite a nota do Pedro: 5 Relatórios de notas Carlos 8.0 Pedro 5.0 .. .. .. Média da classe = ??

# Criamos uma lista de listas vazias para armazenar os nomes e notas dos alunos
alunos = [[], []]

# Loop para coletar informações de 8 alunos
for i in range(8):
    # Pedimos o nome do aluno
    nome = input("Digite o nome do {}º aluno: ".format(i+1))
    
    # Pedimos a nota do aluno
    nota = float(input("Digite a nota do {}: ".format(nome)))
    
    # Adicionamos o nome e a nota às listas correspondentes
    alunos[0].append(nome)  # lista de nomes
    alunos[1].append(nota)  # lista de notas

# Imprimimos os relatórios de notas
print("\nRelatórios de notas")
for i in range(8):
    # Imprimimos o nome e a nota do aluno com uma casa decimal
    print("{} {:.1f}".format(alunos[0][i], alunos[1][i]))

# Calculamos a média da classe
media = sum(alunos[1]) / len(alunos[1])
print("\nMédia da classe = {:.1f}".format(media))