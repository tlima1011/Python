def calcularSalarioLiquido(sb):
    aumento: float; perc_aumento: float; salario: float
    if sb <= 280:
        perc_aumento = 0.20
    elif sb <= 700:
        perc_aumento = 0.15
    elif sb <= 1500:
        perc_aumento = 0.10
    else:
        perc_aumento = 0.05
    aumento = sb * perc_aumento
    salario = aumento + sb
    perc_aumento *= 100
    return f'Salario Bruto R${sb:.2f}\n' \
           f'Aumento R${aumento:.2f}\n' \
           f'Porcentagem {perc_aumento:.0f}%\n' \
           f'Novo Salário R${salario:.2f}'


salario = float(input('Informe o salario R$'))
print(calcularSalarioLiquido(salario))

