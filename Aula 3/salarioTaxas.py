valorPorHora = float(input('Digite quanto você ganha por hora : '))
horasTrabalhadas = int(input('Digite o número de horas trabalhadas no mês: '))

salarioBruto = valorPorHora * horasTrabalhadas
contribuicaoINSS = salarioBruto * 0.08
taxaSindical = salarioBruto * 0.05
salarioLiquido = salarioBruto - (contribuicaoINSS + taxaSindical)

print(f'Valor do salário bruto: R$ {salarioBruto:.2f}\nvalor da contribuição ao INSS: R$ {contribuicaoINSS:.2f}\nvalor da taxa sindical: R$ {taxaSindical:.2f}\nO valor do salário líquido: R$ {salarioLiquido:.2f}')