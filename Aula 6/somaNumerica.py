soma = 0
num = 1

for den in range(1,51):
    soma += num/den
    if den != 50:
        print(f'{num} / {den} + ', end=' ')
    else:
        print(f'{num} / {den} = ', end=' ')
    num+= 2
print(soma)