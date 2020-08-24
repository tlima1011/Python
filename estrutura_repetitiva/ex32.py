def calcularPrecoCq(q):
    return 1.20 * q


def calcularPrecoBs(qtde):
    return 1.30 * qtde


def calcularPrecoBo(qtde):
    return 1.50 * qtde


def calcularPrecoHam(qtde):
    return 1.20 * qtde


def calcularPrecoCheese(qtde):
    return 1.30 * qtde


def calcularPrecoRefrigerante(qtde):
    return 1.00 * qtde


def somarPrecos(calcularPrecoCq, calcularPrecoBs, precoBo, precoHamburguer, precoCheeseburguer, precoRefrigerante):
    return calcularPrecoCq + calcularPrecoBs + precoBo + precoHamburguer + precoCheeseburguer + precoRefrigerante

linhas = '-=' * 20
print(linhas)
print('Especificação    Código      Preço')
print(linhas)
print('Cachorro Quente  100         R$ 1.20')
print('Bauru Simples    101         R$ 1.30')
print('Bauru com ovo    102         R$ 1.50')
print('Hambúrguer       103         R$ 1.20')
print('Cheeseburguer    104         R$ 1.30')
print('Refrigerante     105         R$ 1.00')
print(linhas)
valorPagar = qtde = preco = codigo = precoCq = precoBo = precoBs = precoHamburguer = precoCheeseburguer = precoRefrigerante = 0
cont = 'S'

while cont == 'S':
    codigo = int(input('Informe o código: '))
    if codigo == 100:
        qtde = int(input('Qual quantidade de Cachorro Quente: '))
        precoCq = calcularPrecoCq(qtde)
    elif codigo == 101:
        qtde = int(input('Qual quantidade de Bauru Simples: '))
        precoBs = calcularPrecoBs(qtde)
    elif codigo == 102:
        qtde = int(input('Qual quantidade Bauru com ovo: '))
        precoBo = calcularPrecoBo(qtde)
    elif codigo == 103:
        qtde = int(input('Qual quantidade Hambúrguer: '))
        precoHamburguer = calcularPrecoHam(qtde)
    elif codigo == 104:
        qtde = int( input('Qual quantidade Cheeseburguer: '))
        precoCheeseburguer = calcularPrecoCheese(qtde)
    elif codigo == 105:
        qtde = int(input('Qual quantidade Refrigerante: ' ) )
        precoRefrigerante = calcularPrecoRefrigerante( qtde )
    else:
        print('Inválido, informe um código válido de 100 a 105: ')

    preco = somarPrecos(precoCq, precoBo, precoBs, precoHamburguer, precoCheeseburguer, precoRefrigerante)
    cont = str(input('Deseja continuar [S][N]: ').upper().strip()[0])
print(f'Valor a Pagar R${preco:.2f}')
