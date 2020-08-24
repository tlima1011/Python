def informarMaiorMenor(n):
    maior: int; menor: int
    maior = 0
    menor = 0
    for i in range(0, n):
        numero = int(input(f'Informe o {i+1}º número: '))
        if i == 0:
            maior = numero
            menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
    return f'Maior número {maior}\nMenor número: {menor}'


n = int(input('Informar número de termos: '))
print(informarMaiorMenor(n))