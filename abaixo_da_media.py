n: int; media: float; soma: float

media = soma = 0.0

n = int(input('Quantos elementos vai ter o vetor? '))

numeros: [float] = [0 for x in range(n)]

for i in range(0, n):
    numeros[i] = float(input(f'Digite {i + 1 }º número: '))

for nums in numeros:
    soma += nums

media = soma / n

print(f'\nMEDIA DO VETOR = {media:.3f}') #12.125
print('ELEMENTOS ABAIXO DA MEDIA:')
for nums in numeros:
    if nums < media:
        print(f'{nums:.1f}')

#10.0
#9.8