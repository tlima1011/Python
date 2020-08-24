def informarMaior(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


def informarMenor(a, b, c):
    if a < b and a < c:
        return a
    elif b < c:
        return b
    else:
        return c


a = int(input('Informe o A: '))
b = int(input('Informe o B: '))
c = int(input('Informe o C: '))
print(f'O maior número {informarMaior(a,b,c)}')
print(f'O menor número {informarMenor(a,b,c)}')