def main():
    C = int(input())

    for i in range(C):
        palavra = input()
        mensagem = ''
        for letra in palavra:
           if is_lower_letter(letra):
              mensagem += f'{letra}'

        mensagem_invertida = mensagem [::-1]
        print(mensagem_invertida)
              

def is_lower_letter(char):
  return ord(char) >= 97 and ord(char) <= 122

main()