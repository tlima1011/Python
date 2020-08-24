def informarPeriodo(d):
    if d == 'M':
        return 'Bom Dia'
    elif d == 'V':
        return 'Boa Tarde'
    elif d == 'N':
        return 'Boa Noite'
    else:
        return 'Inválido'


dia = str(input('''
Infome o periodo do dia 
[M] - Matutino
[V] - Vespertino
[N] - Noturno: ''').upper()[0])
print(informarPeriodo(dia))
#M-matutino ou V-Vespertino ou N- Noturno