def consoanteVogal(l):
    if l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U':
        return f'A letra {l} é vogal'
    else:
        return f'A letra {l} é consoante'


letra = str(input('Informe uma letra: ').upper()[0])
print(consoanteVogal(letra))

