x: int; y: int; troca: int; soma: int

soma = 0

print('Digite dois numeros: ')
x = int(input())
y = int(input())

if x > y:
    troca = x
    x = y
    y = troca

for i in range(x + 1, y):
    if i % 2 != 0:
        soma += i

print(f'SOMA DOS IMPARES = {soma}')