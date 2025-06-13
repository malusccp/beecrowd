salario = float(input())
imposto = 0.0
if salario <= 2000:
    print('Isento')
else:
    if salario > 4500:
       imposto += (salario - 4500) * 28/100  
       salario = 4500
    if salario > 3000:
        imposto += (salario - 3000) * 18/100
        salario = 3000
    if salario > 2000:
       imposto += (salario - 2000) * 8/100

    print(f'R$ {imposto:.2f}')