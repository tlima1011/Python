codigo: int; alcool: int; gasolina: int; diesel: int
codigo = alcool = gasolina = diesel = 0

while codigo != 4:
    codigo = int(input('Informe um codigo (1, 2, 3) ou 4 para parar:'))# 8
    if codigo == 1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1
print('\nMUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')



