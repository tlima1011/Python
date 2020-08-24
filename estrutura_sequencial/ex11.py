n1: int; n2: int; n3:float


def calcularNumero(n1, n2, n3):
    from math import pow

    res1 = n1 * 2 * (n3 / 2.0)
    res2 = n2 * 3 + n3
    res3 = pow(n3, 3)
    return f"Resultado 1: {res1:.1f} \nResultado 2: {res2:.1f} \nResultado 3: {res3:.1f}"


n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo numero: '))
n3 = float(input('Informe o terceiro número: '))
print(calcularNumero(n1, n2, n3))