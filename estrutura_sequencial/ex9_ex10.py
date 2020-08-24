def converterCf(c):
    return c * (9 / 5.0) + 32

def converterFc(f):
    return 5 * (f - 32) / 9.0

tipo = 0
while tipo != 3:
    tipo = int(input('''
Informe o tipo de conversao: 
[1] - Celsius para Farhenheit
[2] - Farhenheit para Celsius
[3] - Sair: '''))
    if(tipo == 1):
        f = float(input('Informe o grau em Farhenheit: '))
        print(f'Em graus celsius {converterFc(f):.1f}')
    elif(tipo == 2):
        c = float(input('Informe o grau em Celsius: '))
        print(f'Em graus farhenheit {converterCf(c):.1f}')
print('Bye...')
