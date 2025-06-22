# Timelimit: 1
# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

# Entrada
# Quatro números inteiros representando a hora de início e fim do jogo.

# Saída
# Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

hour_start, min_start, hour_end, min_end = map(int, input().split())

min_start = hour_start * 60 + min_start
min_end = hour_end * 60 + min_end

duracao = min_end - min_start
if duracao <= 0:
    duracao += 24 * 60
hours = duracao // 60
minutes = duracao % 60

print(f'O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)')