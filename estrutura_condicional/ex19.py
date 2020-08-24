def somar(n1, n2):
    soma = n1 + n2
    resultado: str
    print(f'Soma = {soma}')
    if soma % 2 == 0:
        resultado = 'É par '
        if soma > 0:
            resultado += ' e positivo'
        else:
            resultado += ' e negativo'
    else:
        resultado = 'É impar'
        if soma > 0:
            resultado += ' e positivo'
        else:
            resultado += ' e negativo'
    return resultado


def subtrair(n1, n2):
    sub = n1 - n2
    resultado: str
    print(f'Subtração = {sub}')
    if sub % 2 == 0:
        resultado = 'É par '
        if sub > 0:
            resultado += ' e positivo'
        else:
            resultado += ' e negativo'
    else:
        resultado = 'É impar'
        if sub > 0:
            resultado += ' e positivo'
        else:
            resultado += ' e negativo'
    return resultado


def multiplicacao(n1, n2):
    multi = n1 * n2
    resultado: str
    print(f'Multiplicação = {multi}')
    if multi % 2 == 0:
        resultado = 'É par '
        if multi > 0:
            resultado += ' e positivo'
        else:
            resultado += ' e negativo'
    else:
        resultado = 'É impar'
        if multi > 0:
            resultado += ' e positivo'
        else:
            resultado += ' e negativo'
    return resultado


def divisao(n1, n2):
    divi = n1 / n2
    resultado: str
    print(f'Divisão = {divi}')
    if divi % 2 == 0:
        resultado = 'É par '
        if divi > 0:
            resultado += ' e posirivo'
        else:
            resultado += ' e negativo'
    else:
        resultado = 'É impar'
        if divi > 0:
            resultado += ' e posirivo'
        else:
            resultado += ' e negativo'
    return resultado


codigo:int
codigo = 0
while codigo != 5:
    codigo = (int(input('''Informe a operação:  
    [1] - Soma 
    [2] - Subtação 
    [3] - Multiplicação 
    [4] - Divisão 
    [5] - Sair: ''')))
    if codigo == 1:
        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('Informe o segundo número: '))
        print(somar(num1, num2))
    elif codigo == 2:
        num1 = int( input( 'Informe o primeiro número: '))
        num2 = int( input( 'Informe o segundo número: '))
        print(subtrair(num1, num2))
    elif codigo == 3:
        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('Informe o segundo número: '))
        print(multiplicacao(num1, num2))
    elif codigo == 4:
        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('Informe o segundo número: '))
        print(divisao(num1, num2))
    else:
        break



