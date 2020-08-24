def mostrarTabuada(t):
    produto: int
    linhas = '=' * 13
    print(linhas)
    print(f'Tabuada de {t}')
    print(linhas)
    for i in range(1, 11):
        produto = t * i
        print(f'{t} x {i} = {produto}')
    return linhas


tabuada = int(input('Informe o número da tabuada: '))
print(mostrarTabuada(tabuada))
