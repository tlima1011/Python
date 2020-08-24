def informarMedia(n):
    media: float; soma: float
    soma = 0
    media = 0
    for i in range(0, n):
        numero = int(input(f'Informe o {i+1}º número: '))
        soma += numero
    media = soma / n
    return f'Media = {media:.1f}'


n = int(input('Informar número de termos: '))
print(informarMedia(n))