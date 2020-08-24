def informarTabela(n):
    linhas = '-' * 15
    print(linhas)
    print('Lojas Quase Dois - Tabela de preços')
    print(linhas)
    preco = 1.99
    for i in range(1, n+1):
        print(f'{i} - R${preco:.2f}')
        preco += 1.99
    return linhas

n = int(input('Informar número de preços: '))
print(informarTabela(n))

