# João quer montar um painel de leds contendo diversos números. Ele não possui muitos leds, e não tem certeza se conseguirá montar o número
# desejado. Considerando a configuração dos leds dos números abaixo, faça um algoritmo que ajude João a descobrir a quantidade de leds necessário 
# para montar o valor.

# Obs.: Para programadores de Javascript, recomenda-se o uso de "input.trim().split('\n')" para evitar erros conhecidos.


# Entrada
# A entrada contém um inteiro N, (1 ≤ N ≤ 1000) correspondente ao número de casos de teste, seguido de N linhas, cada linha contendo um número 
# (1 ≤ V ≤ 10100) correspondente ao valor que João quer montar com os leds.

# Saída
# Para cada caso de teste, imprima uma linha contendo o número de leds que João precisa para montar o valor desejado, seguido da palavra "leds".
qtd_leds = {
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6,
    '0': 6
 }

def main():
    N = int(input())

    for i in range(N):
        V = input()
        total_leds = 0
        for num in V:
            total_leds += qtd_leds[num]

        print(f'{total_leds} leds')

main()