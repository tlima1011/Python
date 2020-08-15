distancia: float
combustivel: float
consumo: float

distancia = float(input('Distancia percorrida: '))
combustivel = float(input('Combustível gasto: '))

consumo = distancia / combustivel

print(f'Consumo medio = {consumo:.3f}')