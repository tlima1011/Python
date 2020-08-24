def calcularAnos(popA, txA, popB, txB):
    anos = 0
    while popA <= popB:
        popA = popA + (popA * txA)
        popB = popB + (popB * txB)
        anos += 1
    return f'A população de A chegar em B é de {anos} anos.'


popA = int(input('Informe a população A: '))
txA = float(input('Informe a taxa de população de A: '))
popB = int(input('Informe a população B: '))
txB = float(input('Informe a taxa de população de B: '))
while popA > popB:
    print('Inválido população de A, não pode ser de B: ')
    popA = int(input('Informe a população A: ' ) )
    txA = float(input('Informe a taxa de população de A: '))
    popB = int(input('Informe a população B: ' ) )
    txB = float(input('Informe a taxa de população de B: '))
print(calcularAnos(popA, txA, popB, txB))