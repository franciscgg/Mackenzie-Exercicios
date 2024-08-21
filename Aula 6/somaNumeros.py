soma = 0
print('Digite 5 números:')
for num in range(0,5,1):
    num = int(input())
    soma = soma + num
print(f'Soma = {soma}')