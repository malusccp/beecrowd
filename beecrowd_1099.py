# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y.
# Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

# Entrada
# A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linh
# contendo dois inteiros X e Y.

# Saída
# Imprima a soma de todos valores ímpares entre X e Y.

def main():
    N = int(input())

    for i in range(N):
        X, Y = map(int, input().split())

        if X > Y:
            X, Y = Y, X

        soma = 0
        
        for num in range(X+1, Y):
            if num % 2 != 0:
                soma += num
        print(soma)

main()