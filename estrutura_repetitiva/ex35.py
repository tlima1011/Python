def mostrarSerie(n):
    print('S =', end=' ')
    den = num = 1
    soma = somNum =  somaDen = 0
    for i in range(1, n+1):
        print(f'{num}/{den}', end='')
        num += 1
        den += 2
        if i < n:
            print(' +', end=' ')
        else:
            print('.', end='')
        somNum += num
        somaDen += den
        soma = somNum + somaDen
    print(f'\nSoma Numerador: {somNum}')
    print(f'Soma denominador: {somaDen}')
    return f'Soma Termos = {soma}'
    #1 / 1 + 2 / 3 + 3 / 5 + 4 / 7 + 5 / 9 + ... + n / m.


n = int(input('Informe o número de termos: '))
print(mostrarSerie(n))