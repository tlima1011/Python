def calcularCombustivel(t):
    desconto = 0
    precoUnitario = 0
    precoTotal = 0
    litros = 0
    if t == 'A':
        precoUnitario = 1.90
        litros = float(input('Quantos litros de Alcool: '))
        if litros < 20:
            desconto = 0.03
        else:
            desconto = 0.05
        precoUnitario = precoUnitario * litros
        precoTotal = precoUnitario - (precoUnitario * desconto)
        return f'Valor a Pagar de Alcool: R${precoTotal:.2f}'
    else:
        precoUnitario = 2.50
        litros = float(input('Quantos litros de Gasolina: '))
        if litros < 20:
            desconto = 0.04
        else:
            desconto = 0.06
        precoUnitario = precoUnitario * litros
        precoTotal = precoUnitario - (precoUnitario * desconto)
        return f'Valor a Pagar de Gasolina: R${precoTotal:.2f}'


tipo = 'S'
while tipo != 'A' and tipo != 'G':
    tipo = str(input('''Informe o tipo de combustivel: 
[A] - Álcool
[G] - Gasolina: ''').upper().strip()[0])
    if tipo != 'A' and tipo != 'G':
        print('Inválido, informe o tipo de Gasolinha [G] / Alcool [A]: ')
    else:
        print(calcularCombustivel(tipo))