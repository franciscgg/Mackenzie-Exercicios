def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

def menu():
    print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair')
    menuOperacao = int(input())
    while menuOperacao < 1 or menuOperacao > 5:
        print('Opção inválida')
        menuOperacao = int(input())
    return menuOperacao

def operacao(menuOperacao, num1, num2):
    if menuOperacao == 1:
        result = soma(num1, num2)
    elif menuOperacao == 2:
        result = subtracao(num1, num2)
    elif menuOperacao == 3:
        result = multiplicacao(num1, num2)
    elif menuOperacao == 4:
        if num2 != 0:
            result = divisao(num1, num2)
        else:
            result = None
    return result

def entrada():
    return int(input())

def main():
    while True:
        op = menu()
        if op == 5:
            break
        print('Digite o primeiro número:')
        num1 = entrada()
        print('Digite o segundo número: ')
        num2 = entrada()
        resultado = operacao(op, num1, num2)
        if resultado is None:
            print('Não há divisão por zero')
        else:
            print(f'Resultado da sua operação: {resultado}')

main()
