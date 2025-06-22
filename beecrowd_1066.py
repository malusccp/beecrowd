# Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, 
# quantos valores digitados foram positivos e quantos valores digitados foram negativos.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.


positivos = 0
pares = 0
impar = 0
negativos = 0
for i in range(5):
    num = float(input())
    if num > 0: 
        positivos +=1
    if num < 0: 
        negativos += 1
    if num % 2 != 0:
        impar +=1
    if num % 2 == 0:
        pares +=1 
print(f'{pares} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')