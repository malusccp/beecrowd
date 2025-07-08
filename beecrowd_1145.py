# Escreva um programa que leia dois valores X e Y. A seguir, m
# Entrada
# Mostre uma sequência de 1 até Y, passando para a próxima linha a cada X números.

# O arquivo de entrada contém dois valores inteiros, (1 < X < 20) e (X < Y < 100000).

# Saída
# Cada sequência deve ser impressa em uma linha apenas, com 1 espaço em branco entre cada número, conforme exemplo abaixo. Não deve haver espaço 
# em branco após o último valor da linha.

def main():

    X, Y = map(int, input().split())
    saida = ''

    for i in range(1, Y+1, 1):
        if i % X == 0:
            saida += f'{i}'
            print(saida)
            saida = ''
        else:
            saida += f'{i} '


main()