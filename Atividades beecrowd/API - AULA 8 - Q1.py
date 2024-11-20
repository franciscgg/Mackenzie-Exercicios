def adicionarVenda(produtos, vendas):
    for i in range(5):
        produto = input()
        quantidade = int(input())
        produtos.append(produto)
        vendas.append(quantidade)

def produtoMaisVendido(produtos, vendas):
    maxVendas = max(vendas)
    return produtos[vendas.index(maxVendas)], maxVendas

def produtoMenosVendido(produtos, vendas):
    minVendas = min(vendas)
    return produtos[vendas.index(minVendas)], minVendas

produtos = []
vendas = []

adicionarVenda(produtos, vendas)

maisVendido, qtdMais = produtoMaisVendido(produtos, vendas)
menosVendido, qtdMenos = produtoMenosVendido(produtos, vendas)

print(f"{maisVendido} {qtdMais}")
print(f"{menosVendido} {qtdMenos}")
