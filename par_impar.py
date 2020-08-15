n: int; numero: int; resultado: str;

n = int(input('Quantos numeros voce vai digitar? '))

for i in range(1, n+1):
    numero = int(input(f'Digite {i}º numero: '))
    if numero == 0:
        print('NULO')
    elif numero % 2 != 0:
        resultado = 'IMPAR '
        if numero < 0:
            resultado += 'NEGATIVO'
            print(resultado)
        else:
            resultado += 'POSITIVO'
            print(resultado)
    else:
        resultado = 'PAR '
        if numero < 0:
            resultado += 'NEGATIVO'
            print(resultado)
        else:
            resultado += 'POSITIVO'
            print(resultado)

