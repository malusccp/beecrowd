# Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

# Entrada
# A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
# Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
 

# Saída
# Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.

N = int(input())
num_in = 0
num_out = 0
for i in range(1, N+1):
    X = int(input())
    if X >= 10 and X <= 20:
        num_in += 1
    else: 
        num_out += 1

print(f'{num_in} in')
print(f'{num_out} out')    