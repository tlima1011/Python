n: int; pares: int

pares = 0

n = int(input('Quantos numeros voce vai digitar? '))

numeros: [int] = [0 for x in range(n)]

for i in range(0, n):
    numeros[i] = int(input(f'Digite {i + 1}º numero: '))

print('\nNUMEROS PARES:')
for i in range(0, n):
    if numeros[i] % 2 == 0:
        print(f'{numeros[i]} ', end='')
        pares += 1
print()
print(f'\nQUANTIDADE DE PARES = {pares}') #4