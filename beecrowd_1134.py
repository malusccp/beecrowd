
alcool = 0
gasolina = 0
diesel = 0
while True:
    combustivel = int(input())

    if combustivel == 1: alcool += 1
    elif combustivel == 2: gasolina += 1
    elif combustivel == 3: diesel += 1
    elif combustivel == 4: break
    else:
        continue

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')
        