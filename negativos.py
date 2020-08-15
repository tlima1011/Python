n = int

n = int(input('Quantos numeros voce vai digitar? '))

numeros: [int] = [0 for x in range(n)]

for i in range(0, len(numeros)):
    numeros[i] = int(input(f'Digite {i + 1}º numero:: '))

print('\nNUMEROS NEGATIVOS:')
for i in range(0, len(numeros)):
    if numeros[i] < 0:
        print(numeros[i])
# 8
'''Digite um numero: -2
Digite um numero: 9
Digite um numero: 10
Digite um numero: -3
Digite um numero: -7


-2
-3
-7'''