def darVeredito(telefonou, local, mora, deve, trabalhou):
    total = 0
    pontoTelefonou = 0
    pontoLocal = 0
    pontoMora = 0
    pontoDeve = 0
    pontoTrabalhou = 0
    if telefonou == 'S':
        pontoTelefonou += 1
    if local == 'S':
        pontoLocal += 1
    if mora == 'S':
        pontoMora += 1
    if deve == 'S':
        pontoDeve += 1
    if trabalhou == 'S':
        pontoTrabalhou += 1
    total = pontoTelefonou + pontoLocal + pontoMora + pontoDeve + pontoTrabalhou
    if total == 0 or total == 1:
        return 'Inocente'
    elif total == 2:
        return 'Suspeita'
    elif total == 3 or total == 4:
        return 'Cumplice'
    elif total == 5:
        return 'Assassino'


telefonou = str(input("Telefonou para a vítima? ").upper()[0])
local = str(input("Esteve no local do crime? ").upper()[0])
mora = str(input("Mora perto da vítima? ").upper()[0])
deve = str(input("Devia para a vítima? ").upper()[0])
trabalhou = str(input("Já trabalhou com a vítima? ").upper()[0])
print(f'Veredito: {darVeredito(telefonou, local, mora, deve, trabalhou)}')


"""O programa deve no final emitir
uma classificação sobre a participação da pessoa no crime. Se
a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5
como "Assassino". Caso contrário, ele será classificado como
"Inocente"."""
