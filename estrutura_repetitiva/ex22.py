def calcularValorCds(n):
    preco = 0
    soma = 0
    media = 0
    for i in range(0, n):
        preco = float(input(f'Informe o preço do {i + 1}º em R$'))
        soma += preco
    media = soma / n
    return f'Preço Total dos CDs R${soma:.2f}'


n = int(input( 'Informe a quantidade de CDs: ' ))
print(calcularValorCds(n))




