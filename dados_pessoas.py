n: int; menor: float; maior: float; mulheres : int; homens: int;
media_mulheres: float; soma_mulheres : float

media_mulheres = soma_mulheres = mulheres = homens = 0

n = int(input('Quantos alunos serao digitados? '))

alturas: [float] = [0 for x in range(n)]
generos : [str] = [0 for x in range(n)]

for i in range(0, n):
    alturas[i] = float(input(f'Altura da {i + 1}ª pessoa: '))
    generos[i] = str(input(f'Genero da {i + 1}ª pessoa: ').upper()[0])

menor = alturas[0]
maior = alturas[0]

for a in alturas:
    if a > maior:
        maior = a
    if a < menor:
        menor = a

print(f'\nMenor altura = {menor:.2f}') # 1.54
print(f'Maior altura = {maior:.2f}') #1.83

for i in range(0, n):
    if generos[i] == 'M':
        homens += 1
    elif generos[i] == 'F':
        mulheres += 1
        soma_mulheres += alturas[i]
media_mulheres = soma_mulheres / mulheres

print(f'Media das alturas das mulheres = {media_mulheres:.2f}') # 1.69
print(f'Numero de homens = {homens}') #2