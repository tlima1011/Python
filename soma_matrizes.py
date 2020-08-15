m: int; n: int

m = int(input('Quantas linhas vai ter cada matriz?  '))#2
n = int(input('Quantas colunas vai ter cada matriz? '))#3

a: [[int]] = [[0 for x in range(n)] for x in range(m)]
b: [[int]] = [[0 for x in range(n)] for x in range(m)]
c: [[int]] = [[0 for x in range(n)] for x in range(m)]

print('Digite os valores da matriz A:')
for i in range(0, m):
    for j in range(0, n):
        a[i][j] = int(input(f'Elemento [{i},{j}]: '))

print('Digite os valores da matriz B:')
for i in range(0, m):
    for j in range(0, n):
        b[i][j] = int(input(f'Elemento [{i},{j}]: '))

for i in range(0, m):
    for j in range(0, n):
        c[i][j] = a[i][j] + b[i][j]

print('MATRIZ SOMA:')
for i in range(0, m):
    for j in range(0, n):
        print(c[i][j], end=' ')
    print()

#5 9 7
#5 13 9