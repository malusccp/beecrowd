# Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês.
# O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

# Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

# Entrada
# Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, 
# será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo 
# formato das duas primeiras linhas, indicando o término do evento.

# Saída
# Na saída, deve ser apresentada a duração do evento, no seguinte formato:

# W dia(s)
# X hora(s)
# Y minuto(s)
# Z segundo(s)

# Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

start = input().split()
day_start = int(start[1])
hours_start, minutes_start, seconds_start = map(int, input().split(' : '))
end = input().split()
day_end = int(end[1])
hours_end, minutes_end, seconds_end = map(int, input().split(' : '))

start_in_sec = day_start * 86400 + hours_start * 3600 +  minutes_start * 60 + seconds_start 
end_in_sec = day_end * 86400 + hours_end * 3600 +  minutes_end * 60 + seconds_end

duracao = end_in_sec - start_in_sec


days = duracao // 86400
hours_remainder = duracao % 86400

hours = hours_remainder // 3600
minutes_remainder = hours_remainder % 3600

minutes = minutes_remainder // 60
seconds = minutes_remainder % 60

print(f'{days} dia(s)')
print(f'{hours} hora(s)')
print(f'{minutes} minuto(s)')
print(f'{seconds} segundo(s)')