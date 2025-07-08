# Dados três valores, verifique se os três podem formar um triângulo. Em caso afirmativo, verifique se ele é escaleno, isóceles ou equilátero 
# e se trata-se de um triângulo retângulo ou não.

# Entrada
# A entrada consiste em três números inteiros A,B e C (0 < A,B,C < 105).

# Saída
# A saída deve conter a string "Invalido" se os valores lidos não formarem um triângulo. Se os valores formarem um triângulo a saída deve ser 
# "Valido-Equilatero", "Valido-Escaleno" ou "Valido-Isoceles" de acordo com a característica do triângulo seguido de "Retangulo: S" se o triângulo
# for retângulo ou "Retangulo: N" se não for, conforme os exemplos.

def main():
      A, B, C = map(int, input().split())
      if eh_triangulo(A, B, C):
         if equilatero(A,B,C):
            print('Valido-Equilatero')
         elif escaleno(A,B,C):
               print('Valido-Escaleno')
         elif isoceles(A,B,C):
               print('Valido-Isoceles')

         if eh_retangulo(A,B,C):
            print('Retangulo: S')
         else:
            print('Retangulo: N')
      else:
         print('Invalido')
      

def eh_triangulo(A, B, C): 
  return A < B + C and B < A + C and C < A + B

def equilatero(A, B, C):
   return A == B and B ==C and A == C

def escaleno(A, B,C):
   return A != B and B != C and  A != C
   
def isoceles(A, B, C):
   return A == B or B == C or A == C
   
def eh_retangulo(A,B,C):
    lados = sorted([A, B, C])
    return lados[2]**2 == lados[0]**2 + lados[1]**2
   
main()