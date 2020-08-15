c: float; f : float;
escala: str

escala = str(input('Voce vai digitar a temperatura em qual escala [C/F]? ')).upper()[0]

if escala == 'F':
    f = float(input('Digite a temperatura em Fahrenheit: '))#75.00
    c = 5 / 9 * (f - 32)
    print(f'Temperatura equivalente em Celsius: {c:.2f}ºC')
else:
    c = float(input('Digite a temperatura em Celsius: '))
    f = c * 9 / 5.0 + 32
    print(f'Temperatura equivalente em Fahrenheit: {f:.2f}')
