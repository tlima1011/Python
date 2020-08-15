n: int; linha: int; coluna: int; soma: float

soma = 0
n = int(input('Qual a ordem da matriz?  '))#3

mat: [[float]] = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = float(input(f'Elemento [{i},{j}]: '))

for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] > 0:
            soma += mat[i][j]

print(f'\nSOMA DOS POSITIVOS: {soma:.1f}')

linha = int(input('\nEscolha uma linha: '))
print('LINHA ESCOLHIDA: ', end='')
for j in range(0, n):
    print(f'{mat[linha][j]:.1f}', end='  ')
print()
coluna = int(input('\nEscolha uma coluna: '))
print('COLUNA ESCOLHIDA: ', end='')
for i in range(0,n):
    print(f'{mat[i][coluna]:.1f}', end='  ')

print()
print(f'\nDIAGONAL PRINCIPAL: ', end='')
for i in range(0, n):
    print(f'{mat[i][i]:.1f}', end='  ')

print()
print(f'\nMATRIZ ALTERADA: ', end='')
for i in range(0,n):
    for j in range(0,n):
        if mat[i][j] < 0:
            print(f'{pow(mat[i][j]):.1f}  ')
        else:
            print(f'{mat[i][j]:.1f}  ')
    print()
'''Elemento [0,0]: 7.0
Elemento [0,1]: -8.0
Elemento [0,2]: 10.0
Elemento [1,0]: -2.0
Elemento [1,1]: 3.0
Elemento [1,2]: 5.0
Elemento [2,0]: 11.0
Elemento [2,1]: -15.0
Elemento [2,2]: 4.0

SOMA DOS POSITIVOS: 40.0

Escolha uma linha: 1
LINHA ESCOLHIDA: -2.0 3.0 5.0

Escolha uma coluna: 2
COLUNA ESCOLHIDA: 10.0 5.0 4.0

DIAGONAL PRINCIPAL: 7.0 3.0 4.0

MATRIZ ALTERADA:
7.0 64.0 10.0
4.0 3.0 5.0
11.0 225.0 4.0'''