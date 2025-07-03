def main():
  qtd = int(input())

  while qtd > 0:
    numero = int(input())
    tipo = 'EVEN' if numero % 2 == 0 else 'ODD'

    if numero > 0:
      print(f'{tipo} POSITIVE')
    elif numero < 0:
      print(f'{tipo} NEGATIVE') 
    else:
      print('NULL')

    qtd -= 1


main()