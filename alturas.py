n: int; media: float; soma: float

porc = cont = soma = media = 0

n = int(input('Quantas pessoas serao digitadas? '))

nomes: [float] = [0 for x in range(n)]
alturas: [float] = [0 for x in range(n)]
idades: [float] = [0 for x in range(n)]

for i in range(0, n):
    print(f'Dados da {i + 1}ª pessoa: ')
    nomes[i] = str(input('Nome: '))
    idades[i] = int(input('Idade: '))
    alturas[i] = float(input('Altura: '))

for i in range(0, n):
    soma += alturas[i]

media = soma / n
print(f'\nAltura média: {media:.2f}')

for i in range(0, n):
    if idades[i] < 16:
        cont += 1

porc = cont * 100 / n
print(f'Pessoas com menos de 16 anos: {porc:.1f}%')

for i in range(0,n):
    if idades[i] < 16:
        print(f'{nomes[i]}')

