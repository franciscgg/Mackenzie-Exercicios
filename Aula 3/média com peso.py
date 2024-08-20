print('Digite 3 notas')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
print('Digite o peso das 3 notas')
peso1 = int(input('Digite o peso da primeira nota: '))
peso2 = int(input('Digite o peso da segunda nota: '))
peso3 = int(input('Digite o peso da terceira nota: '))

media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)


print(f'A média das notas com peso {media:.1f}')