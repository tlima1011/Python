def informarSalario(s):
    porc = 0.015
    novoSalario = 0
    for i in range(1996, 2020):
        novoSalario = s + (s * porc)
    return f'Novo Salário em 2020 - R${novoSalario:.2f}'


salario = float(input('Informe o salário em 1996 R$'))
print(informarSalario(salario))


