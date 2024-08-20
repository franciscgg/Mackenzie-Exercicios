produto = float(input('Digite o preço da etiqueta do produto: '))
cod = int(input('Digite o código de 1 a 4: '))

if cod == 1:
    desconto = produto * 0.90
    print(f'Á vista em dinheiro ou débito, recebe 10% de desconto: R$ {desconto:.2f}')
elif cod == 2:
    desconto = produto * 0.95
    print(f'Á vista no cartão de crédito, recebe 5% de desconto: R$ {desconto:.2f}')
elif cod == 3:
    parcelado = produto / 2
    print(f'Em 2 vezes, preço normal da etiqueta sem juros: 2x R${parcelado:.2f}')
elif cod == 4:
    parcelado = produto * 1.10 / 3
    print(f'Em 3 vezez, preço normal de etiqueta mais juros de 10%: 3x R${parcelado:.2f} com juros')
else:
    print('Opção inválida')