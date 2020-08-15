n: int; f: int

f = 1
n = int(input(f'Digite o valor de N: '))

for i in range(1, n+1):
    f *= i

print(f'FATORIAL = {f}') #24