n: int; soma: int

soma = 0

n = int(input('Qual a ordem da matriz? ')) #4

mat: [[int]] = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = int(input(f'Elemento [{i},{j}]: '))

for i in range(0, n):
    for j in range(0, n):
        if i < j:
            soma += mat[i][j]

print(f'SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {soma}')

'''Elemento [0,0]: 5
Elemento [0,1]: 2
Elemento [0,2]: 3
Elemento [0,3]: 1
Elemento [1,0]: 8
Elemento [1,1]: 2
Elemento [1,2]: 4
Elemento [1,3]: 5
Elemento [2,0]: 7
Elemento [2,1]: 3
Elemento [2,2]: 1
Elemento [2,3]: 3
Elemento [3,0]: 9
Elemento [3,1]: 12
Elemento [3,2]: 9
Elemento [3,3]: 5
SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = 18'''