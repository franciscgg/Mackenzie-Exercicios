preco = float(input())
cod = int(input("1.Á vista\n2.No Cartão de crédito\n3.No cartão de crédito  5 vezes\n4.No cartão de crédito 10 vezes\n"))

if cod == 1:
    soma = preco - (preco * 0.10)

if cod == 2:
    soma = preco - (preco * 0.05)

if cod == 3:
    soma = preco / 5

if cod == 4:
    soma = (preco / 10) + (preco / 10 * 0.15)

print(f"{soma:.2f}")