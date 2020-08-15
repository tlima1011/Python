a: float; b: float; c: float
areaQuadrado: float; areaTrapezio: float; areaTriangulo:float

a = float(input('Digite a medida A: '))
b = float(input('Digite a medida B: '))
c = float(input('Digite a medida C: '))

areaQuadrado = a * a
areaTriangulo = (a * b) / 2
areaTrapezio = c * (a + b) / 2

print(f'AREA DO QUADRADO = {areaQuadrado:.4f}')
print(f'AREA DO TRIANGULO = {areaTriangulo:.4f}')
print(f'AREA DO TRAPEZIO = {areaTrapezio:.4f}')
#7.0000
# 19.5000
