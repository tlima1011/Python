def parOuImpar(n):
    if n % 2 == 0:
        return 'É par'
    else:
        return 'É impar'


n = int(input('Informe um número: '))
print(parOuImpar(n))
