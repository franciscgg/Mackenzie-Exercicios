valorPremio = 780000.00
primeiroGanhar = 46
segundoGanhador = 32
valorPrimeiro = (primeiroGanhar / 100) * valorPremio
valorSegundo = (segundoGanhador / 100) * valorPremio
valorTerceiro = valorPremio - (valorSegundo + valorPrimeiro)

print(f'Primeiro ganhador ficou com R$ {valorPrimeiro:.2f} \nSegundo ganhador ficou com R$ {valorSegundo:.2f} \nTerceiro ganhador ficou com R$ {valorTerceiro:.2f}')