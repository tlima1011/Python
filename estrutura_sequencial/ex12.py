altura: float;


def calcularPesoIdeal(a):
    return (72.7 * a) - 58


altura = float(input('Informe a altura: '))
print(f"Peso Ideal: {calcularPesoIdeal(altura):.1f}kg")
