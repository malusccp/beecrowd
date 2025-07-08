# Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só que o tamanho de cada um dos 
# dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os 
# próximos números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os 
# valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.

# Entrada
# A entrada contém 15 números inteiros.

# Saída
# Imprima a saída conforme o exemplo abaixo

def main():
    par = []
    impar = []
    for i in range(15):
        num = int(input())
        if num % 2 == 0:
            par.append(num)
            if len(par) == 5:
                for i in range(0, 5, 1):
                    print(f'par[{i}] = {par[i]}')
                par = []
        else:
            impar.append(num)
            if len(impar) == 5:
                for i in range(0, 5, 1):
                    print(f'impar[{i}] = {impar[i]}')
                impar = []
    for j in range(len(impar)):
        print(f"impar[{j}] = {impar[j]}")
    for j in range(len(par)):
        print(f"par[{j}] = {par[j]}")
main()