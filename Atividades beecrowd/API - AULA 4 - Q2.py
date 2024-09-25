entrada = int(input("1. Poupança\n2. CDB\n3. Tesouro Direto\n"))
valor = float(input("Digite o valor: "))
meses = int(input("Digite a quantidade de meses: "))

if entrada == 1:
	taxaJuros = 0.005

elif entrada == 2:
	taxaJuros = 0.008

elif entrada == 3:
	taxaJuros = 0.01

soma = valor * (1 + taxaJuros) ** meses
print(f"R$ {soma:.2f}")