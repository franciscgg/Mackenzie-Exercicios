def Banco():
	saldoInicial = 1000.00
	while True:
		# Mostra o saldo atual antes de realizar uma operação
		print(f"Saldo atual: R$ {saldoInicial:.2f}")

		# Leitura da opção do usuário
		opcao = int(input("Escolha uma opção:\n"
						  "1. Mostrar Saldo\n"
						  "2. Sacar\n"
						  "3. Depositar\n"
						  "4. Sair\n"))
		if opcao == 4:
			break
		elif opcao == 1:
			print(f"Saldo atual: R$ {saldoInicial:.2f}")
		elif opcao == 2:
			valorSacar = float(input("Digite o valor para saque: "))
			if valorSacar <= saldoInicial:
				saldoInicial -= valorSacar
		elif opcao == 3:
			valorDepositar = float(input("Digite o valor para depósito: "))
			saldoInicial += valorDepositar

Banco()
