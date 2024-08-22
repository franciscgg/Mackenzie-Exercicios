import random

quantidade = int(input('Digite quantos números inteiros aleatórios quer que seja gerado entre (1 a 10): '))
soma = 0
for ct in range(quantidade):
    numero = random.randint(1,10)
    print(f'Número gerado: {numero}')
    soma += numero
print(f'Soma dos números gerados: {soma}')
