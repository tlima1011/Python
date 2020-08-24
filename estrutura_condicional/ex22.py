def calcularValor(kgMorango, kgMaca):
    precoTotal = 0
    kgTotal = 0
    precoKgMorango = 0
    precoUnitarioMorango = 0
    precoKgMaca = 0
    precoUnitarioMaca = 0
    if kgMorango < 5:
        precoUnitarioMorango = 2.50
    else:
        precoUnitarioMorango = 2.20
    if kgMaca < 5:
        precoUnitarioMaca = 1.80
    else:
        precoUnitarioMaca = 1.50
    precoKgMorango = precoUnitarioMorango * kgMorango
    precoKgMaca = precoUnitarioMaca * kgMaca
    kgTotal = kgMorango + kgMaca
    precoTotal = precoKgMaca + precoKgMorango
    return f'Kg de morango: {kgMorango:.1f}kg - R${precoKgMorango:.2f}\n' \
           f'Kg de maçâ: {kgMaca:.1f}kg - R${precoKgMaca:.2f}\n' \
           f'Kg Total {kgTotal:.1f}kg - R${precoTotal:.2f}'


print('QUINTANDA + BARATO!!!')
kgMorango = float(input('Quantos kg de morango:'))
kgMaca = float(input('Quantos kg de maçã: '))
print(calcularValor(kgMorango,kgMaca))