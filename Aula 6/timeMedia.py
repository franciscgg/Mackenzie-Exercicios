soma_geral = 0
ct = 0

for time in range(4):
    print(f'Time {time+1}')
    soma = 0
    for jogador in range (2):
        print(f'Idade do jogador {jogador+1}')
        idade = int(input())
        if idade < 18:
            ct+=1
        soma += idade
    print(f'Média de idade do time {time+1} é igual a {soma/2:.0f} anos')
    soma_geral += soma
print(f'Média dos atletas do campeonato é igual a {soma_geral/8:.0f} anos')
print(f'Quantidade de atletas menor de idade é igual a {ct}')