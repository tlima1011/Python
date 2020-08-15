n: int; qtde: int; tipo: str; coelhos: int; ratos: int; sapos: int; total: int;
porc_coelhos: float; porc_sapos: float; porc_ratos: float

total = ratos = coelhos = sapos = qtde = 0

n = int(input('Quantos casos de teste serao digitados? '))

for i in range(0, n):
    qtde = int(input('Quantidade de cobaias: '))
    tipo = str(input('Tipo de cobaia: [C] - Coelhos [R] - Ratos [S] - Sapos: ').upper()[0])
    if tipo == 'C':
        coelhos += qtde
    elif tipo == 'R':
        ratos += qtde
    elif tipo == 'S':
        sapos += qtde
    else:
        while tipo != 'C' and tipo != 'S' and tipo != 'R':
            print('Invalido digite novamente...')
            tipo = str(input('Tipo de cobaia: [C] - Coelhos [R] - Ratos [S] - Sapos: ').upper()[0])

total = coelhos + ratos + sapos
porc_coelhos = coelhos / total * 100
porc_ratos = ratos / total * 100
porc_sapos = sapos / total * 100

print('RELATORIO FINAL:')
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {porc_coelhos:.2f}%')
print(f'Percentual de ratos: {porc_ratos:.2f}%')
print(f'Percentual de sapos: {porc_sapos:.2f}%')

