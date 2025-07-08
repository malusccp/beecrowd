# Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., até trocar 
# o 10º com o 11º. Mostre o vetor modificado.

# Entrada
# A entrada contém 20 valores inteiros, positivos ou negativos.

# Saída
# Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.

def main():
    N = criar_lista()
    for i in range(10):
        N[i], N[5-i] = N[5-i], N[i]

    for i in range(20):
        print(f'N[{i}] = {N[i]}')


def criar_lista():
    N = []
    for _ in range(20):
        num = int(input())
        N.append(num)
    return N

main()