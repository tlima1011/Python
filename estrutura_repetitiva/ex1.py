def validacaoNota(n):
    while 0 < n > 10:
        if 0 < n > 10:
            n = float(input('Inválido, informe novamente: '))
    return 'Nota válida'


nota = float(input('Informe um nota: '))
print(validacaoNota(nota))

"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o
usuário informe um valor válido."""

