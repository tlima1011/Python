def informarNumerosDecrescente(n1, n2, n3):
    if n1 > n2 and n1 > n3 and n2 > n3:
        return f'{n1}, {n2}, {n3}'
    elif n1 > n2 and n1 > n3 and n3 > n2:
        return f' {n1}, {n3}, {n2}'
    elif n2 > n1 and n2 > n3 and n1 > n3:
        return f'{n2}, {n1}, {n3} '
    elif n2 > n1 and n2 > n3 and n3 > n1:
        return f'{n2}, {n3}, {n1}'
    elif n3 > n1 and n3 > n2 and n1 > n2:
        return f'{n3}, {n1}, {n2}'
    else:
        return f' {n3}, {n2}, {n1}'


num1 = int(input('Informe o número 1: '))
num2 = int(input('Informe o número 2: '))
num3 = int(input('Informe o número 3: '))
print(informarNumerosDecrescente(num1, num2, num3))