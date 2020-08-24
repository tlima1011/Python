def anoBissexto(a):
    if a % 400 == 100 or a % 4 == 0:
        return 'Ano é bissexto'
    else:
        return 'Não é bissexto'


ano = int(input('Informe o ano: '))
print(anoBissexto(ano))