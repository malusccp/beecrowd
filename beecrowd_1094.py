# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual 
# ela é responsável. Ela quer saber no final do ano, quantas cobaias 
# foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

# Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que 
# foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

# Entrada
# A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro 
# Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

# Saída
# Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que 
# o percentual deve ser apresentado com dois dígitos após o ponto.

def main():
    N = int(input())

    total_cobaias = 0
    coelhos = 0
    ratos = 0
    sapos = 0
    porc_c = 0
    porc_r = 0
    porc_s = 0

    for experimentos in range(1, N+1):
        qtd_cobaias, tipo_cobaia = map(str, input().split())
        total_cobaias += int(qtd_cobaias)
    
        if tipo_cobaia == 'C': coelhos += int(qtd_cobaias)
        elif tipo_cobaia == 'S': sapos += int(qtd_cobaias)
        elif tipo_cobaia == 'R': ratos += int(qtd_cobaias)

    print(f'Total: {total_cobaias} cobaias')
    print(f'Total de coelhos: {coelhos}')
    print(f'Total de ratos: {ratos}')
    print(f'Total de sapos: {sapos}')
    print(f'Percentual de coelhos: {percentual(coelhos, total_cobaias):.2f} %')
    print(f'Percentual de ratos: {percentual(ratos, total_cobaias):.2f} %')
    print(f'Percentual de sapos: {percentual(sapos, total_cobaias):.2f} %')
def percentual (parte, todo):
    return (parte/todo) * 100
main()