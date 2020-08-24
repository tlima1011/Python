def informarPrimo(n):
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont += 1
    if cont == 2:
        return f'O número {n} é primo'
    else:
        return f'O número {n} não é primo'


n = int(input('Informe um número: '))
print(informarPrimo(n))