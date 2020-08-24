def calcularPreco(t):
    troco = 0
    dinheiro = 0
    dinheiro = float(input('Dinheiro: R$')) #R$ 20.00
    troco = dinheiro - t
    print(f'Total: R${t:.2f}')  # 9.00
    print(f'Dinheiro: R${dinheiro:.2f}')
    return f'Troco: R${troco:.2f}' #11.00


print('Lojas Tabajara')
preco = 2
i = 1
total = 0
while preco != 0:
    preco = float(input(f'Produto {i}: R$'))
    total += preco
    i += 1
print(calcularPreco(total))



