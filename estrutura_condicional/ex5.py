def informarAprovacao(n1, n2):
    media = (n1 + n2) / 2.0
    print(f'Média {media:.1f}')
    if media < 7.0:
        return "Reprovado"
    elif media < 10:
        return "Aprovado"
    else:
        return "Aprovado com distinção"


nota1 = float(input('Infore a primeira nota: '))
nota2 = float(input('Infore a segunda nota: '))
print(informarAprovacao(nota1, nota2))
