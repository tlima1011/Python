def informarTemperaturas(n):
    media = menor = maior = soma = 0
    for i in range(0, n):
        temp = float(input(f'Informe a {i + 1}ª temperatura: '))
        soma += temp
        if i == 0:
            maior = temp
            menor = temp
        else:
            if temp > maior:
                maior = temp
            if temp < menor:
                menor = temp
    media = soma / n
    return f'Menor temperatura: {menor:.1f}ºC \
           \nMaior temperatura: {maior:.1f}ºC \
           \nMedia temperatura: {media:.1f}ºC'


n = int(input('Informe o número de temperaturas: '))
print(informarTemperaturas(n))
