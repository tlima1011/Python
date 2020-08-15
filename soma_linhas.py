n: int; m: int

m = int(input('Qual a quantidade de linhas da matriz? '))
n = int(input('Qual a quantidade de colunas da matriz? '))

mat: [[float]] = [[0 for x in range(n)] for x in range(m)]
vet: [float] = [0 for x in range(m)]

for i in range(0, m):
    print(f'Digite os elementos da {i + 1}ª linha:')
    for j in range(0, n):
        mat[i][j] = float(input())

for i in range(0, m):
    for j in range(0, n):
        vet[i] += mat[i][j]

print('VETOR GERADO:')
for i in range(0, m):
    print(f'{vet[i]:.1f}')

#25.0
#10.0