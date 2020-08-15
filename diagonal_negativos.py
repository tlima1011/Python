n: int; negativos: int

negativos = 0
n = int(input('Qual a ordem da matriz? '))

mat = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = int(input(f'Elemento [{i},{j}]: '))

print('\nDIAGONAL PRINCIPAL: ', end='')
for i in range(0, n):
    print(f'{mat[i][i]} ', end='')

for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] < 0:
            negativos += 1

print(f'\nQUANTIDADE DE NEGATIVOS = {negativos}')