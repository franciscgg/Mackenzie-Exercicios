contador = 0
somas = []

while True:
    N = input()
    if N == "fim":
        break
    qtd = int(input())
    valor = float(input())
    soma = valor * qtd
    somas.append(soma)
    contador += soma
for soma in somas:
    print(f"{soma:.2f}")
print(f"{contador:.2f}")
