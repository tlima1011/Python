unitario: float; dinheiro: float; preco: float; troco: float; faltante: float
quantidade: int

unitario = float(input('Preço unitário do produto R$'))
quantidade = int(input('Quantidade comprada: '))
dinheiro = float(input('Dinheiro recebido: R$'))
preco = quantidade * unitario

if dinheiro < preco:
    faltante = preco - dinheiro
    print(f'DINHEIRO INSUFICIENTE, FALTAM R${faltante:.2f}') #20.00 REAIS
else:
    troco = dinheiro - preco
    print(f'TROCO = R${troco:.2f}')
 #4.00
'''Exemplo 2:
Preço unitário do produto: 30.00
Quantidade comprada: 3
Dinheiro recebido: 70.00

Problema "'''