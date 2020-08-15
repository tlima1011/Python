salario: float; aumento: float; porc: float; novoSalario: float

salario = float(input('Digite o salario da pessoa R$'))

if salario <= 1000:
    porc = 0.20
elif salario <= 3000:
    porc = 0.15
elif salario <= 8000:
    porc = 0.10
else:
    porc = 0.05

aumento = salario * porc
porc *= 100
novoSalario = salario + aumento

print(f'\nSalario Atual R${salario:.2f}')
print(f'Novo salario = R${novoSalario:.2f}')
print(f'Aumento R${aumento:.2f}')
print(f'Porcentagem = {porc:.0f}%')

'''
Salário atual 
Aumento
Até R$ 1000.00 20%
Acima de R$ 1000.00
até R$ 3000.00
15%
Acima de R$ 3000.00
até R$ 8000.00
10%
Acima de R$ 8000.00 5%

'''
