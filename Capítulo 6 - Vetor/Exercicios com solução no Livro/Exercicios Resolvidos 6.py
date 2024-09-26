# Faça um programa que calcula e mostra um vetor em ordem decrescente de um outro vetor já definido.

# Vetor de números
Vetor = [3, 5, 4, 2, 1, 6, 8, 7, 11, 9]

# Ordena o vetor em ordem decrescente (reversa) usando a função sorted
vetor_sorted = sorted(Vetor, reverse=True)

# Imprime o vetor original e o vetor ordenado
print(f"Vetor não Organizado {Vetor}")
print(f"Vetor Reverso e Organizado {vetor_sorted}")