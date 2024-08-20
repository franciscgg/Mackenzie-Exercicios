import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b ** 2 -4 * a * c

if delta > 0:
   x1 = (-b + math.sqrt(delta)) / (2 * a)
   x2 = (-b - math.sqrt(delta)) / (2 * a)
   print(f'Raízes reais distintas: x1 = {x1} e x2 = {x2}')
elif delta == 0:
    x = -b / (2 * a)
    print(f'Raiz real dupla: x = {x}')
else:
    print('Não há raízes reais.')