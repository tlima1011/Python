n: int; abaixo: int; acima: int; entre: int
lucroTotal: float; lucro_compra: float; lucro_venda: float; lucro: float; percentualLucro: float

percentualLucro = acima = entre = abaixo = lucro_compra = lucro_venda = lucroTotal = 0

n = int(input('Quantos alunos serao digitados? '))

nomes: [str] = [0 for x in range(n)]
precoCompra: [float] = [0 for x in range(n)]
precoVenda: [float] = [0 for x in range(n)]

for i in range(0, n):
    print(f'Produto {i+1}:')
    nomes[i] = input('Nome: ')
    precoCompra[i] = float(input('Preco de compra: R$'))
    precoVenda[i] = float(input('Preco de venda: R$'))

for i in range(0, n):
    lucro = precoVenda[i] - precoCompra[i]
    percentualLucro = lucro * 100 / precoCompra[i]
    if percentualLucro < 10:
        abaixo += 1
    elif percentualLucro <= 20:
        entre += 1
    else:
        acima += 1

for i in range(0, n):
    lucro_compra += precoCompra[i]
    lucro_venda += precoVenda[i]
    lucroTotal = lucro_venda - lucro_compra

print('RELATORIO:')
print(f'Lucro abaixo de 10%: {abaixo}')
print(f'Lucro entre 10% e 20%: {entre}')
print(f'Lucro acima de 20%: {acima}')
print(f'Valor total de compra: R${lucro_compra:.2f}')#30.00
print(f'Valor total de venda: R${lucro_venda:.2f}') #33.50
print(f'Lucro total: R${lucroTotal:.2f}')