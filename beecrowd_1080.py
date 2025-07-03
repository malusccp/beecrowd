# Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

# Entrada
# O arquivo de entrada contém 100 números inteiros, positivos e distintos.

# Saída
# Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

def main():
    posicao = 0
    maior = 0
    for i in range(1, 100):
        numero = int(input())
        if numero > maior:
            maior = numero
            posicao = i
    print(maior)
    print(posicao)

main()