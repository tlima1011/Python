n: int; numero: int; media: float; nota1: float; nota2: float; nota3: float

n = int(input('Quantos casos voce vai digitar?'))

for i in range(0, n):
    print('Digite tres numeros: ')
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    media = (2 * nota1 + 3 * nota2 + 5 * nota3)/10
    print(f'MEDIA = {media:.1f}') #5.7
