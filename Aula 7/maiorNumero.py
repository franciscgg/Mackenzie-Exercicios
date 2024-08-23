def entrada():
    print ('Digite o primeiro número: ')
    num1 = int(input())
    print('Digite o segundo número: ')
    num2 = int(input())
    return num1,num2

def maiorNumero(num1, num2):
    if num1 > num2:
       return num1
    else:
        return num2

def main():
    num1, num2 = entrada()
    numeroMaior = maiorNumero(num1, num2)
    print(f'O número maior é: {numeroMaior}')

main()
