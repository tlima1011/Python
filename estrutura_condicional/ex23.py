def calcularValor(kgFileDuplo, kgAlcatra, kgPicanha):
    cartao: str; card: str
    card = "Não"
    precoTotal = 0
    valorPagar = 0
    precoKgFileDuplo = 0
    precoKgAlcatra = 0
    precoKgPicanha = 0
    precoUnitarioFileDuplo = 0
    precoUnitarioAlcatra = 0
    precoUnitarioPicanha = 0
    desconto = 0
    if kgFileDuplo < 5:
        precoUnitarioFileDuplo = 4.90
    else:
        precoUnitarioFileDuplo = 5.80
    if kgAlcatra < 5:
        precoUnitarioAlcatra = 5.90
    else:
        precoUnitarioAlcatra = 6.80
    if kgPicanha < 5:
        precoUnitarioPicanha = 6.90
    else:
        precoUnitarioPicanha = 7.80
    precoKgFileDuplo = precoUnitarioFileDuplo * kgFileDuplo
    precoKgAlcatra = precoUnitarioAlcatra * kgAlcatra
    precoKgPicanha = precoUnitarioPicanha * kgPicanha
    kgTotal = kgFileDuplo + kgAlcatra + kgPicanha
    precoTotal = precoKgFileDuplo + precoKgAlcatra + precoKgPicanha
    cartao = str(input('Possui o Cartão Tabajara SuperDescontos? ').upper().strip()[0])
    if cartao == 'S':
        desconto = 0.05
        card = 'Sim'

    valorPagar = precoTotal - (precoTotal * desconto)
    return f'Kg de Filé Duplo: {kgFileDuplo:.1f}kg - Preço Filé Duplo: R${precoKgFileDuplo:.2f}\n' \
           f'Kg de Alcatra: {kgAlcatra:.1f}kg - Preço Alcatra: R${precoKgAlcatra:.2f}\n' \
           f'Kg de Picanha: {kgPicanha:.1f}kg - Preço Picanha: R${precoKgPicanha:.2f}\n' \
           f'Kg Total: {kgTotal:.1f}kg - Preço Total: R${precoTotal:.2f}\n' \
           f'Cartão Tabajara - {card}\n' \
           f'Desconto - {desconto * 100:.0f}%\n' \
           f'Valor Pagar R${valorPagar:.2f}'


kgFileDuplo = float(input('Kg de Filé Duplo: '))
kgAlcatra = float(input('Kg de Alcatra: '))
kgPicanha = float(input('Kg de Picanha: '))
print(calcularValor(kgFileDuplo, kgAlcatra, kgPicanha))


