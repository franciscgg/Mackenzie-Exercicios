valor = float(input('Valor da conta: '))
divisao = valor/3
cada = int(divisao)
sobra = valor - 2 * cada

print(f'Carlos irá pagar R$ %.2f' %cada)
print(f'André irá pagar R$ %.2f' %cada)
print(f'Felipe irá pagar R$ %.2f' %sobra)