# Escreva um programa que leia um valor inteiro N (1 < N < 1000). Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

# Entrada
# O arquivo de entrada contém um número inteiro positivo N.

# Saída
# Imprima a saída conforme o exemplo fornecido.

def main():
    N = int(input())

    x = 1
    for linhas in range(N):
        print(f'{x**1} {x**2} {x**3}')
        x +=1

main()