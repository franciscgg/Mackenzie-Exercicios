def areaQuadrado(lado):
    return lado ** 2

def entrada():
 lado = float(input('Lado:'))
 return lado

def main():
    lado = entrada()
    area = areaQuadrado(lado)
    print(f'Área: {area}')

main()