n: int; maior: int; pos_maior: int

maior = pos_maior = 0

n = int(input('Quanto numeros voce vai digitar? '))

numeros: [float] = [0 for x in range(n)]
for i in range(0, n):
    numeros[i] = float(input('Digite um numero: '))

maior = numeros[0]
pos_maior = 0

for i in range(1,n):
    if numeros[i] > maior:
        maior = numeros[i]
        pos_maior = i

print(f'\nMAIOR VALOR = {maior:.1f}')#14.0
print(f'POSICAO DO MAIOR VALOR = {pos_maior}')#3