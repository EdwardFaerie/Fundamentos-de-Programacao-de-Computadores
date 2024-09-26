# Faça um programa que leia um vetor com quinze posições para números inteiros. Crie, a seguir, um vetor resultante que contenha todos os números primos do vetor digitado. Escreva o vetor resultante.

# Definimos uma função para verificar se um número é primo
def e_primo(n):
    # Se o número for menor ou igual a 1, não é primo
    if n <= 1:
        return False
    
    # Verificamos se o número é divisível por qualquer número entre 2 e a raiz quadrada do número
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            # Se o número for divisível, não é primo
            return False
    
    # Se o número não for divisível por nenhum número, é primo
    return True

# Inicializamos dois vetores vazios para armazenar os elementos
vetor = []
vetor_primos = []

# Preenchemos o vetor com 15 elementos
print("Preencha o vetor:")
for i in range(15):
    # Pedimos o elemento ao usuário
    elemento = int(input("Digite o {}º elemento: ".format(i+1)))
    
    # Adicionamos o elemento ao vetor
    vetor.append(elemento)

# Criamos o vetor de números primos usando a função e_primo
vetor_primos = [elemento for elemento in vetor if e_primo(elemento)]

# Imprimimos o vetor resultante com números primos
print("\nVetor resultante com números primos:")
print(vetor_primos)