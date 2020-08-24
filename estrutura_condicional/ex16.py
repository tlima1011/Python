def calcularEquacao(a,b,c):
    from math import pow, sqrt
    delta: float; x1: float; x2: float
    delta = pow(b,2) - 4 * a * c
    if a == 0 or delta < 0:
        return 'Não existe raízes reais'
    else:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        return f'X1 = {x1:.4f}\nX2 = {x2:.4f}'


a = float(input('Informe o coeficiente A: '))
b = float(input('Informe o coeficiente B: '))
c = float(input('Informe o coeficiente C: '))
print(calcularEquacao(a,b,c))