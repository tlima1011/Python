def informarFibonacci(n):
    n1: int; n2: int; n3:int
    n1 = 0
    n2 = 1
    for i in range(0,n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=' ')
    return '=> Acabou'


n = int(input('Informar o número de termos: '))
print(informarFibonacci(n))