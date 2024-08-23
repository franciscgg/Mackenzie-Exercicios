def multiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

def entrada():
    print ('Digite o primeiro número: ')
    num1 = int(input())
    print('Digite o segundo número: ')
    num2 = int(input())
    return num1,num2

def main():
    num1, num2 = entrada()
    print(multiplo(num1,num2))

main()