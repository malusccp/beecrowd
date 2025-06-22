# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, 
# uma linha em branco e em seguida, os valores na sequência como foram lidos.

# Entrada
# A entrada contem três números inteiros.

# Saída
# Imprima a saída conforme foi especificado.

A, B, C = map(int, input().split())

menor = A
if B < menor:
    menor = B
if C < menor:
    menor = C

maior = A
if B > maior: 
    maior = B
if C > maior:
    maior = C

meio = A + B + C - maior - menor

print(menor)
print(meio)
print(maior)
print()
print(A)
print(B)
print(C)


