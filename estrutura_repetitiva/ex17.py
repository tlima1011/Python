def calcularFatorial(n):
    print(f'{n}! = ', end=' ')
    f = 1
    for i in range(n, 0, -1):
        if i == 1:
            print(f'{i} = ', end=' ')
        else:
            print(f'{i} . ', end='')
        f *= i
    return f


numero = int(input('Informe o número para fatorial: '))
print(calcularFatorial(numero))
