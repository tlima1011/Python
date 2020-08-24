def informarParesImpares(n):
    nums: int; pares: int; impares: int
    pares = 0
    impares = 0
    for i in range(0, n):
        nums = int(input(f'Informe o {i+1}º número: '))
        if nums % 2 == 0:
            pares += 1
        else:
            impares += 1
    return f'Pares: {pares}\nImpares: {impares}'


n = int(input('Informe o número de termos: '))
print(informarParesImpares(n))