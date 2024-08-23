def atualizarPreco(produto):
    return produto + (produto * 0.10)

def taxa(produto):
    precoAtualizado = atualizarPreco(produto)
    return precoAtualizado * 0.025

def main():
    produto = float(input('Digite o valor do produto: R$ '))
    precoAtualizado = atualizarPreco(produto)
    precoTaxa = taxa(produto)
    valorFinal = precoAtualizado + precoTaxa
    print(f'Valor do produto: R$ {produto:.2f}')
    print(f'Produto com aumento: R$ {precoAtualizado:.2f}')
    print(f'Valor da taxa: R$ {precoTaxa:.2f}')
    print(f'Produto com aumento e a taxa: R$ {valorFinal:.2f}')

main()
