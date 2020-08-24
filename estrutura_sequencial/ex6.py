def calcularArea(r):
    from math import pi, pow
    return pi * pow(r, 2)


raio = float(input('Informe o raio.: '))
print(f'Area do circulo {calcularArea(raio):.1f}')