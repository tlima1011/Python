def calcularPotencia(base, expoente):
    potencia: int
    potencia = 1
    for i in range(1, expoente+1):
        potencia *= base
    return potencia


base = int(input('Informe a base: '))
expoente = int(input('Informe expoente: '))
print(f'Potencia = {calcularPotencia(base,expoente)}')