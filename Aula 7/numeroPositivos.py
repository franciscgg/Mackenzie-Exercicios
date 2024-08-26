def entrada():
    n= -1
    while n<=0:
        n= int(input('Digite um número inteiro e positivo: '))
        return n

def contaDivisor(n):
    ndiv = 0
    for cont in range (1,n+1):
        resto= n%cont
        if resto == 0:
            ndiv += 1
    return ndiv

def main():
    n = entrada()
    print(contaDivisor(n))

main()