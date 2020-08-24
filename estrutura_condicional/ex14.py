def calcularAproveitamento(n1,n2):
    conceito: str;
    media = (n1 + n2) / 2.0
    if media >= 0 and media <= 4:
        conceito = 'E'
    elif media <= 6:
        conceito = 'D'
    elif media <= 7.5:
        conceito = 'C'
    elif media <= 9:
        conceito = 'B'
    else:
        conceito = 'A'
    print(f'Media = {media:.1f}')
    print(f'Conceito {conceito}')
    if conceito == 'E' or conceito == 'D':
        return 'REPROVADO'
    else:
        return 'APROVADO'


nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
print(calcularAproveitamento(nota1, nota2))