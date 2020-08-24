def informarNumsImpares(n):
    for i in range(0, n):
        if i % 2 != 0:
            print(i)
    return '<= terminou'


n = int(input('Informe a quantidade de termos: '))
print(informarNumsImpares(n))