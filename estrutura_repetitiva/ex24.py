def informarTabela(n):
    linhas = '-' * 55
    preco = 0.18
    print(linhas)
    print(f'Panificadora Pão de Ontem - Tabela de preços\nPreço do pão R${preco:.2f}')
    print(linhas)
    for i in range(1, n+1):
        print(f'{i} - R${preco:.2f}')
        preco += 0.18
    return linhas


n = int(input('Informar número de preços: '))
print(informarTabela(n))