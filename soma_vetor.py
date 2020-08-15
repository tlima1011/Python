n: int; soma: int; media:float

soma = media = 0

n = int(input('Quantos numeros voce vai digitar? '))

numeros = [0 for x in range(n)]

for i in range(0, n):
    numeros[i] = float(input(f'Digite {i + 1}º numero: '))

print('\nVALORES = ', end='')
for i in range(0, n):
    print(f'{numeros[i]:.1f}  ', end='')
    soma += numeros[i]
media = soma / n
print(f'\nSOMA = {soma:.2f}')
print(f'MEDIA = {media:.2f}')
'''Digite um numero: 4.0
Digite um numero: 10.0
Digite um numero: 14.0
 8.0 4.0 10.0 14.0
SOMA = 36.00
MEDIA = 9.00'''