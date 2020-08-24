def calcularMediaIdades(n):
    '''
    :var: Número de idades a serem calculadas
    :param n: número de idades
    :return: retorna se a média de idade é jovem, adulta, velha
    :name: Thiago
    '''
    soma = 0
    media = 0
    for i in range(0, n):
        idade = int(input(f'Informe a {i + 1}ª idade: '))
        soma += idade
    media = soma / n
    if media <= 25:
        return 'A média de idade é jovem'
    elif media <= 60:
        return 'A média de idade é adulta'
    else:
        return 'A média de idade é idosa'


n = int(input('Informe o número de idades: '))
print(calcularMediaIdades(n))


