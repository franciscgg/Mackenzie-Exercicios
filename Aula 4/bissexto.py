ano = int(input('Insira o ano a ser analisado: '))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto')