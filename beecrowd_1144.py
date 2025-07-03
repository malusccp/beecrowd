# Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída serão apresentadas na execução do programa, seguindo a lógica do exemplo abaixo. 
# Para valores com mais de 6 dígitos, todos os dígitos devem ser apresentados.

# Entrada
# O arquivo de entrada contém um número inteiro positivo N (1 < N < 1000).

# Saída
# Imprima a saída conforme o exemplo fornecido.

def main():
    N = int(input())
    x = 1

    for linhas in range(1, N*2+1):
        if linhas % 2 != 0: 
            print(f'{x**1} {x**2} {x**3}')
        elif linhas % 2 == 0:
            print(f'{x} {x**2 + 1} {x**3 + 1}')
            x += 1

main()