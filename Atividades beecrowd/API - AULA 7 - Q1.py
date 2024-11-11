def eh_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    a = int(input())
    b = int(input())
    c = int(input())

    if eh_triangulo(a, b, c):
        print("Os lados formam um triângulo")
        print(tipo_triangulo(a, b, c))
    else:
        print("Os lados não formam um triângulo")

main()
