#import math
#numero = int(input('Digite um número inteiro: '))
#if numero <0:
#    print('Por favor, digite um número inteiro')
#else:
#    fatorial = math.factorial(numero)
#print(f'O fatorial de {numero} é {fatorial}')
from math import factorial

numero = int(input('Digite um número inteiro natural: '))
fatorial = 1
while numero <0:
    numero = int(input())
for x in range (1, numero+1):
    fatorial = fatorial * x
print(f'O fatorial de {numero} é {fatorial}')

