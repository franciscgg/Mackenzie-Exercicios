pares = 0
impares = 0

n = int(input("Digite a quantidade de números:"))

for i in range(n):
	numero = int(input("Digite o número: "))
	if numero % 2 == 0:
		pares += 1
	else:
		impares += 1

print(pares)
print(impares)
