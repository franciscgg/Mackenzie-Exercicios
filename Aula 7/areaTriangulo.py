def areaTriangulo(base,altura):
    area = (base * altura) / 2
    return area

def entrada(texto):
    n = int(input(texto))
    return n

def main():
    base = entrada('Digite o valor da base: ')
    altura = entrada('Digite o valor da altura: ')
    area = areaTriangulo(base,altura)
    print(area)

main()