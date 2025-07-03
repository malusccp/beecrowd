# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas 
# válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

# Entrada
# A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem lidas duas notas válidas.

# Saída
# Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
# Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo. O valor deve ser apresentado com duas casas após o 
# ponto decimal.

def main():
    nota1 = float_in_range(0, 10)
    nota2 = float_in_range(0, 10)

    media = (nota1 + nota2) / 2
    print(f'media = {media:.2f}')
    
    


def float_in_range(min_value, max_value):
    numero = get_float_number()

    while numero > max_value or numero < min_value:
        print('nota invalida')
        numero = get_float_number()
    return numero

    
def get_float_number():
    entrada = input()

    try:
        numero = float(entrada)
        return numero
    except ValueError:
        return get_float_number()

main()
    