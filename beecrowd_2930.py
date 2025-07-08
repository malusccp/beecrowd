# Mostre, para cada caso de teste, se a acadêmica apresentará ou não. A única possibilidade da entrega não ser realizada na data é por falta de 
# orientação da Takanada. Caso não seja possivel, imprima "Eu odeio a professora!". Caso seja entregue em até 3 dias antes do prazo final, imprima 
# "Muito bem! Apresenta antes do Natal!", caso contrário, sendo muito próximo da data limite imprima "Parece o trabalho do meu filho!", nesse ultimo
# caso, é adicionado mais dois dias para correções, e caso a data final seja menor que a véspera do natal(24), ela poderá apresentar, sendo 
# impresso "TCC Apresentado!", caso contrário imprima 
# "Fail! Entao eh nataaaaal!"

def main():
    E, D = map(int, input().split())

    if E > D:
        print('Eu odeio a professora!')
    else:
        if E <= D-3:
            print('Muito bem! Apresenta antes do Natal!')
        else:
            print('Parece o trabalho do meu filho!')
            if E + 2 < 24:
                print('TCC Apresentado!')
            else:
                print('Fail! Entao eh nataaaaal!')

main()