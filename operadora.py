minutos: int; valor: float;

minutos = int(input('Digite a quantidade de minutos: '))
 #22
valor = 50
if minutos > 100:
    valor = valor + 2 * (minutos - 100)

print(f'Valor a pagar: R${valor:.2f}')#50.00