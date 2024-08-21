num = int(input('Digite ps números encerrando com 0: \n'))
maior = num
menor = num
soma = 0

while num != 0:
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    num = int(input())
print(f'Soma {soma}')
print(f'Menor {menor}')
print(f'Maior {maior}')

