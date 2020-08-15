from math import sqrt, pow

base: float; altura: float

base = float(input('Base do retangulo: ')) #4.0
altura = float(input('Altura do retangulo: ')) #5.0

area = base * altura
perimetro = 2 * (base + altura)
diagonal = sqrt(pow(base, 2) + pow(altura, 2))

print(f'AREA = {area:.4f}') #20.0000
print(f'PERIMETRO = {perimetro:.4f}') #18.0000
print(f'DIAGONAL = {diagonal:.4f}') #6.4031