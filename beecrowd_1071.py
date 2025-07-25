# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

# Entrada
# O arquivo de entrada contém dois valores inteiros.

# Saída
# O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.


def main():

    X = int(input())
    Y = int(input())
    
    if X > Y:
        X, Y = Y, X

    soma = 0
        
    for num in range(X+1, Y):
        if num % 2 != 0:
            soma += num
    print(soma)

main()