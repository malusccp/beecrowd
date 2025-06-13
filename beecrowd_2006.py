
cha = int(input())
contador = 0
corretas = 0
competidores = A, B, C, D, E = list(map(int, input().split()))
if cha in competidores: corretas += competidores.count(cha)

print(corretas)
