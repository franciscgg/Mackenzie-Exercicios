n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3

if media >=0 and media <3:
    print(f'Reprovado sua nota foi {media:.1f} na média')
elif media <7:
    print(f'Exame sua nota foi {media:.1f} na média')
else:
    print(f'Aprovado sua nota foi {media:.1f} na média\nParábens!!!')
