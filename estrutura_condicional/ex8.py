def informarMaisBarato(p1, p2, p3):
    if p1 < p2 and p1 < p3:
        return p1
    elif p2 < p3:
        return p2
    else:
        return p3


preco1 = float(input('Informe o preço 1 R$'))
preco2 = float(input('Informe o preço 2 R$' ) )
preco3 = float(input('Informe o preço 3 R$' ) )
print(f'O preço mais barato R${informarMaisBarato(preco1, preco2, preco3):.2f}')