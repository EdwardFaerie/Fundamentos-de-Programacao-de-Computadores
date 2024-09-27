# Uma escola deseja controlar as médias das disciplinas que seus alunos cursam. Sabe-se que nessa escola existem três turmas, com oito alunos cada uma, e cada aluno cursa quatro disciplinas. Crie um programa que armazene essas médias em uma matriz 3  8  4. Depois da leitura, ele deverá calcular e mostrar: ■ a média geral de cada aluno; ■ a média de cada turma.

# Receber as médias das disciplinas de cada aluno
medias = []
for i in range(3):
    turma = []
    for j in range(8):
        aluno = []
        for k in range(4):
            aluno.append(float(input(f"Digite a média da disciplina {k+1} do aluno {j+1} da turma {i+1}: ")))
        turma.append(aluno)
    medias.append(turma)

# Calcular a média geral de cada aluno
media_geral_aluno = []
for i in range(3):
    for j in range(8):
        media_geral_aluno.append(sum(medias[i][j]) / 4)

# Calcular a média de cada turma
media_turma = []
for i in range(3):
    soma = 0
    for j in range(8):
        soma += sum(medias[i][j]) / 4
    media_turma.append(soma / 8)

# Mostrar os resultados
print("Média geral de cada aluno:")
for i in range(3):
    for j in range(8):
        print(f"Aluno {j+1} da turma {i+1}: {media_geral_aluno[i*8 + j]}")

print("\nMédia de cada turma:")
for i in range(3):
    print(f"Turma {i+1}: {media_turma[i]}")