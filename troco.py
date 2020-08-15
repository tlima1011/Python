preco: float
unitario: float
quantidade: int
dinheiro: float

unitario = float(input('Preço unitário do produto R$'))
quantidade = int(input('Quantidade comprada: '))
dinheiro = float(input('Dinheiro recebido: '))

preco = unitario * quantidade
troco = dinheiro - preco

print(f'TROCO = R${troco:.2f}')
 #4.00