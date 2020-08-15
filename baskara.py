from math import sqrt
a: float; b: float; c: float; x1: float; x2: float; delta: float

a = float(input('Coeficiente a: '))
b = float(input('Coeficiente b: '))
c = float(input('Coeficiente c: '))
delta = pow(b, 2) - (4 * a * c)
 #1
 #0
 #-9
if a == 0 or delta < 0:
     print('Esta equacao nao possui raizes reais')
else:
    x1 = (- b + sqrt(delta)) / (2 * a)
    x2 = (- b - sqrt(delta)) / (2 * a)
    print(f'X1 = {x1:.4f}')#3.0000
    print(f'X2 = {x2:.4f}')# -3.0000