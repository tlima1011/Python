numero: int; soma: int;
x = soma = 0

numero = int(input('Digite um numero inteiro: '))

while numero == 0:
    if numero % 2 != 0:
        numero += 1
soma = 5 * numero + 20

print(f'SOMA = {soma}')


