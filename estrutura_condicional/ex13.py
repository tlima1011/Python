def informarDiaSemana(d):
    if d == 1:
        return 'Domingo'
    elif d == 2:
        return 'Segunda'
    elif d == 3:
        return 'Terça'
    elif d == 4:
        return 'Quarta'
    elif d == 5:
        return 'Quinta'
    elif d == 6:
        return 'Sexta'
    else:
        return 'Sábado'


dia = int(input('Informe o dia: '))
print(informarDiaSemana(dia))

