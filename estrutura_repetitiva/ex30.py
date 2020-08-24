def montarTabuada(t,i,f):
    produto = 0
    print(f'Vou montar a tabuada de {t} começando em {i} e terminando em {f}:')
    for i in range(i, f+1):
        produto = t * i
        print(f'{t} x {i} = {produto}')
    return ''


tabuada = int(input('Montar a tabuada de: ')) #5
inicio = int(input('Começar por: '))#4
final = int(input('Terminar em: '))#7
while inicio > final:
    print(f'Inválido, o valor inicial não pode ser maior que o final: ')
    inicio = int(input('Começar por: '))
    final = int(input('Terminar em: '))
print(montarTabuada(tabuada, inicio, final))
