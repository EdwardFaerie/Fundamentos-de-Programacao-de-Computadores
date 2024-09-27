# Faça um programa que preencha uma matriz 10 × 3 com as notas de dez alunos em três provas. O programa deverá mostrar um relatório com o número dos alunos (número da linha) e a prova em que cada aluno obteve menor nota. Ao final do relatório, deverá mostrar quantos alunos tiveram menor nota em cada uma das provas: na prova 1, na prova 2 e na prova 3

import random

# Cria uma matriz 10x3 com notas aleatórias entre 0 e 10
notas = [[random.randint(0, 10) for _ in range(3)] for _ in range(10)]

# Mostra a matriz de notas
print("Matriz de notas:")
for linha in notas:
    print(linha)

# Cria um relatório com o número dos alunos e a prova em que cada aluno obteve menor nota
relatorio = []
for i, linha in enumerate(notas):
    menor_nota = min(linha)
    prova_menor_nota = linha.index(menor_nota) + 1
    relatorio.append(f"Aluno {i+1}: menor nota na prova {prova_menor_nota}")

# Mostra o relatório
print("\nRelatório:")
for linha in relatorio:
    print(linha)

# Conta quantos alunos tiveram menor nota em cada prova
contagem_provas = [0, 0, 0]
for linha in relatorio:
    prova = int(linha.split()[-1]) - 1
    contagem_provas[prova] += 1

# Mostra a contagem de alunos por prova
print("\nContagem de alunos por prova:")
print(f"Prova 1: {contagem_provas[0]} alunos")
print(f"Prova 2: {contagem_provas[1]} alunos")
print(f"Prova 3: {contagem_provas[2]} alunos")