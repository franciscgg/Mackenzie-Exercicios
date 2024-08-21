while True:
    menuOperacao = int(input('1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n0. Sair\n'))
    if menuOperacao == 0:
        print('Programa Encerrado!')
        break
    elif menuOperacao in [1, 2, 3, 4]:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        if menuOperacao == 1:
            resultado = n1 + n2
            operacao = 'soma'
        elif menuOperacao == 2:
            resultado = n1 - n2
            operacao = 'subtração'
        elif menuOperacao == 3:
            resultado = n1 * n2
            operacao = 'multiplicação'
        elif menuOperacao == 4:
            if n1 != 0 and n2 != 0:
                resultado = n1 / n2
                operacao = 'divisão'
            else:
                print('Não há divisão por zero!')
                continue

        print(f'A {operacao} de {n1} e {n2} é igual a {resultado}')
    else:
        print('Digite uma opção válida!')
