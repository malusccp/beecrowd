# Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido,
# mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

# Entrada
# O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

# Saída
# Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

def main():
    while True:
        M, N = map(int, input().split())
        if M <= 0 or N <= 0: break

        if M > N:
            M, N = N, M
        
        soma = 0
        numeros = ''
        for num in range(M, N+1):
            soma += num
            numeros += f'{num} '
        numeros += f'Sum={soma}'
        print(numeros)

main()