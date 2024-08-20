km= int(input('Insira o valor de km: '))
litros = float(input('Insira o valor de litros: '))
consumo = km / litros

if consumo < 8:
    print(f'Venda o carro! {consumo:.2f}KM por 1L')
elif 8 <= consumo < 12:
    print(f'Econômico! {consumo:.2f}KM por 1L')
else:
    print(f'Supereconômico! {consumo:.2f}KM por 1L')