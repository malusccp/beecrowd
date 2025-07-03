# Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.

# Entrada
# A entrada contém um valor inteiro N (N < 10000).

# Saída
# Imprima todos valores que quando divididos por N dão resto = 2, um por linha.

def main():
    N = int(input())

    for num in range(1, 10000+1):
        if num % N == 2:
            print(num)

main()