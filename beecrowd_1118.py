# Escreva um programa para ler as notas da primeira e a segunda avaliação de um aluno. Calcule e imprima a média semestral. O programa só deverá aceitar notas válidas 
# (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

# No final deve ser impressa a mensagem “novo calculo (1-sim 2-nao)”, solicitando ao usuário que informe um código (1 ou 2) indicando se ele deseja ou não executar o
# algoritmo novamente, (aceitar apenas os código 1 ou 2). Se for informado o código 1 deve ser repetida a execução de todo o programa para permitir um novo cálculo, 
# caso contrário o programa deve ser encerrado.

# Entrada
# O arquivo de entrada contém vários valores reais, positivos ou negativos. Quando forem lidas duas notas válidas, deve ser lido um valor inteiro X . O programa deve 
# parar quando o valor lido para este X for igual a 2.

# Saída
# Se uma nota inválida for lida, deve ser impressa a mensagem “nota invalida”. Quando duas notas válidas forem lidas, deve ser impressa a mensagem “media = ” seguido 
# do valor do cálculo.

# Antes da leitura de X deve ser impressa a mensagem "novo calculo (1-sim 2-nao)" e esta mensagem deve ser apresentada novamente se o valor da entrada padrão para X for
# menor do que 1 ou maior do que 2, conforme o exemplo abaixo.

# A média deve ser impressa com dois dígitos após o ponto decimal.

def main():

    media = calculo()

    while True:
        print('novo calculo (1-sim 2-nao)')
        resposta = int_in_range(1,2)
        if resposta == 2: break
        calculo()

def media_nota(nota1, nota2):
    return (nota1 + nota2) / 2

def calculo():
    nota1 = float_in_range(0, 10)
    nota2 = float_in_range(0, 10)

    print(f'media = {media_nota(nota1, nota2):.2f}')

def int_in_range(min_value, max_value):
    numero = get_int_number()

    while numero > max_value or numero < min_value:
        print('novo calculo (1-sim 2-nao)')
        numero = get_int_number()
    return numero

    
def get_int_number():
    entrada = input()

    try:
        numero = int(entrada)
        return numero
    except ValueError:
        return get_int_number()



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