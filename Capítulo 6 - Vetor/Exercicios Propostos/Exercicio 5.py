# Uma escola deseja saber se existem alunos cursando, simultaniamente, as disciplinas Lógica e outra disciplina linguagem de Programação. Coloque os números das matrículas dos alunos que cursam Lógica em um vetor, quinze alunos. Coloque os números das matriculas dos alunos que cursam lingugagem de programação em outro vetor, dez alunos. Mostre o número das matriculas que aparecem nos dois vetores

# Criar vetor de 15 valores de entrada de matriculas de alunos começando de 1 até 16 para alunos de lógica
logica_students = [int(input(f"Digite o número de matricula do aluno de lógica {i}: ")) for i in range(1,16)]

# Mesma coisa que: 
# logica_students = []
# for i in range(1,16):
#     logica_students.append(int(input(f"Digite o número de matricula do aluno de lógica {i}: ")))

# Criar vetor de 10 valores de entrada de número de matriculas de alunos que fazem programação
prog_students = [int(input(f"Digite o número de matricula do aluno de programação {i}: ")) for i in range(1,11)]

# Mesma coisa que: 
# prog_students = []
# for i in range(1,11):
#     prog_students.append(int(input(f"Digite o número de matricula do aluno de programação {i}: ")))

# Verificar se existem números de matriculas iguais nos dois cursos:
common_students = [student for student in logica_students if student in prog_students]

# Mesma coisa que:
# common_students = []
# for indice_logica, aluno_logica in enumerate(logica_students):
#    for indice_prog, aluno_prog in enumerate(prog_students):
#        if aluno_prog == aluno_logica:
#            common_students.append(aluno_logica or aluno_prog)

# Mostrar os alunos que cursam os dois cursos:
print("Alunos que cursam Lógica e Linguagem de Programação:", common_students)