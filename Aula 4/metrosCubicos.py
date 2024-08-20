metrosCubicos = int(input('Consumo em metros cúbicos: '))

if  metrosCubicos < 10:
    conta = 7
    print(f'Valor da conta: R${conta:.2f}')
elif metrosCubicos >= 11 and metrosCubicos <= 30:
    conta = (metrosCubicos - 10) * 1 + 7
    print(f'Valor da conta: R${conta:.2f}')
elif metrosCubicos >= 31 and metrosCubicos <= 100:
    conta = (metrosCubicos - 30) * 2 + 27
    print(f'Valor da conta: R${conta:.2f}')
else:
    conta = (metrosCubicos - 100) * 5 + 167
    print(f'Valor da conta: R${conta:.2f}')