n: int;

n = int(input('Quantos valores vai ter cada vetor? '))

a: [int] = [0 for x in range(n)]
b: [int] = [0 for x in range(n)]
c: [int] = [0 for x in range(n)]

print('Digite os valores do vetor A:')
for i in range(0,n):
    a[i] = int(input())

print('Digite os valores do vetor B: ')
for i in range(0,n):
    b[i] = int(input())

for i in range(0, n):
    c[i] = a[i] + b[i]

print('VETOR RESULTANTE:')
for n in c:
    print(n)
