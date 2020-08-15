quant: int; codigo:int; valor: float;

codigo = int(input('Codigo do produto comprado: '))
if codigo == 1:
    quant = int(input('Quantidade comprada: '))
    valor = 5.00 * quant
    print(f'Valor a pagar: R${valor:.2f}')
elif codigo == 2:
    quant = int(input('Quantidade comprada: '))
    valor = 3.50 * quant
    print(f'Valor a pagar: R${valor:.2f}')
elif codigo == 3:
    quant = int(input( 'Quantidade comprada: '))
    valor = 4.80 * quant
    print(f'Valor a pagar: R${valor:.2f}')
elif codigo == 4:
    quant = int(input( 'Quantidade comprada: '))
    valor = 8.90 * quant
    print(f'Valor a pagar: R${valor:.2f}')
elif codigo == 5:
    quant = int(input( 'Quantidade comprada: '))
    valor = 7.52 * quant
    print(f'Valor a pagar: R${valor:.2f}')
else:
    print('Invalido')
'''1 R$ 5.00
2 R$ 3.50
3 R$ 4.80
4 R$ 8.90
5 R$ 7.32
Valor a pagar: R$ 15.00
'''

