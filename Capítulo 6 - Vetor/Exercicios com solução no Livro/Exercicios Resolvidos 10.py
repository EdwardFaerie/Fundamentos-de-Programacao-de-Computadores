# Faça um programa para corrigir provas de multipla escolha. Cada prova tem 8 questões e cada questão vale um ponto. Existem dez alunos matriculados, calcule e mostre: O numero e nota de cada aluno, a porcentagem de aprovação sabendo que a nota mínima é 6.

# Crie um dicionário vazio para armazenar as informações dos alunos
students = {}

# Crie uma lista vazia para armazenar as respostas do gabarito
gabarito = []

# Loop para preencher o gabarito com as respostas das 8 questões
for num in range(0, 8):
    # Pede ao usuário que digite a resposta da questão atual
    gabarito.append(input(f"Insira a resposta da questão {num+1}: "))

# Loop para preencher o dicionário de alunos com as informações de cada aluno
for num in range(0, 10):
    # Pede ao usuário que digite o nome do aluno atual
    nome = input(f"Insira o nome do aluno {num+1}: ")
    
    # Crie um dicionário vazio para armazenar as informações do aluno atual
    students[nome] = {'acertos': 0, 'questoes': 8}
    
    # Loop para preencher as respostas do aluno atual
    for i in range(0, 8):
        # Pede ao usuário que digite a resposta do aluno atual para a questão atual
        resposta = input(f"Insira a resposta do aluno {nome} para a questão {i+1}: ")
        
        # Verifica se a resposta do aluno atual é igual à resposta do gabarito
        if resposta == gabarito[i]:
            # Se for igual, incrementa o número de acertos do aluno atual
            students[nome]['acertos'] += 1

# Loop para calcular a nota de cada aluno e imprimir o resultado
for nome, aluno in students.items():
    # Crie uma chave 'nota' no dicionário do aluno atual e atribua o valor do número de acertos
    aluno['nota'] = aluno['acertos']
    
    # Verifica se o aluno atual foi aprovado ou reprovado
    if aluno['nota'] >= 6:
        # Se foi aprovado, imprime a mensagem de aprovação
        print(f"Aluno {nome} foi aprovado com nota {aluno['nota']}")
    else:
        # Se foi reprovado, imprime a mensagem de reprovação
        print(f"Aluno {nome} foi reprovado com nota {aluno['nota']}")

# Crie uma variável para armazenar o número de alunos aprovados
approved_students = sum(1 for aluno in students.values() if aluno['nota'] >= 6)

# Crie uma variável para armazenar a porcentagem de aprovação
approval_percentage = (approved_students / len(students)) * 100

# Imprime a porcentagem de aprovação
print(f"Porcentagem de aprovação: {approval_percentage:.2f}%")