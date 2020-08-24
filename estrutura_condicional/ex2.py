def positivoNegativo(n):
    if n > 0:
        return f'O número {n} é positivo'
    else:
        return f'O número {n} é negativo'


num = int(input('Informe um número: '))
print(positivoNegativo(num))


