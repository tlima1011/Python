def termos(n):
    for i in range(1, n+1):
        print(i)

    for i in range(21, 42):
        print(i, end=' ')
    return '<= Acabou'


n = int(input('Informe o número de termos: '))
print(termos(n))