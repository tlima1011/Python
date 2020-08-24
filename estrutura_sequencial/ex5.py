def converterCentimetros(m):
    return m * 100;


metros = float(input('Informe o valor em metros: '))
print(f'Valor em centimetros {converterCentimetros(metros):.1f}cm')
