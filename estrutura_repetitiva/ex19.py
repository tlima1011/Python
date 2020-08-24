def calcularMedia(n):
    soma = 0
    media = 0
    for i in range(0, n):
        notas = float(input(f'Informe a {i + 1}ª nota: '))
        soma += notas
    media = soma / n
    return f'Media {media:.1f}'


n = int(input('Informe o número de notas: '))
print(calcularMedia(n))