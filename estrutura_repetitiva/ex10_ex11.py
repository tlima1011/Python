def informarNums(inicio, final):
    soma: int;
    media: float
    soma = 0
    media = 0
    cont = 0
    for i in range(inicio + 1, final):
        print(i, end=' ')
        soma += i
        cont += 1
    media = soma / cont
    return f'\nSoma = {soma}\nMedia = {media:.1f}'


inicio = int(input('Informar o início: '))
final = int(input('Informar o final: '))
print(informarNums(inicio, final))