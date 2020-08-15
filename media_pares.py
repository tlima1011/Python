n: int; pares: float; media_pares:float; cont: int;

pares = media_pares = cont = 0


n = int(input('Quantos elementos vai ter o vetor? '))
numeros: [int] = [0 for x in range(n)]

for i in range(0, n):
    numeros[i] = int(input(f'Digite {i + 1 }º numero: '))

for nums in numeros:
    if nums % 2 == 0:
        pares += nums
        cont += 1

if cont == 0:
    print('NENHUM NUMERO PAR')
else:
    media_pares = pares / cont
    print(f'MEDIA DOS PARES = {media_pares}')

