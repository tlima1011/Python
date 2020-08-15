from math import pow, pi
raio : float; area: float

raio = float(input('Digite o valor do raio do circulo: '))
area = pi * pow(raio, 2)
#print(pi)
print(f'AREA = {area:.3f}')