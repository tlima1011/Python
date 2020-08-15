m: int; n: int

m = int(input('Qual a quantidade de linhas da matriz? ')) #2
n = int(input('Qual a quantidade de colunas da matriz? '))# 3

mat: [[int]] = [[0 for x in range(n)] for x in range(m)]

for i in range(0, m):
    for j in range(0, n):
        mat[i][j] = int(input(f'Elemento [{i},{j}]: '))

print('VALORES NEGATIVOS:')
for i in range(0, m):
    for j in range(0, n):
        if mat[i][j] < 0:
            print(f'{mat[i][j]}')

'''Elemento [0,0]: 12
Elemento [0,1]: -8
Elemento [0,2]: 5
Elemento [1,0]: -13
Elemento [1,1]: 10
Elemento [1,2]: -6
VALORES NEGATIVOS:
-8
-13
-6'''