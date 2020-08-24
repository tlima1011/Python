def calcularSalarioLiquido(sb):
    inss: float; ir: float; perc_ir : float; sindicato: float; perc_sindicato: float; desconto: float; perc_inss:float
    perc_ir = 0.11
    perc_inss = 0.08
    perc_sindicato = 0.05
    ir = sb * perc_ir
    inss = sb * perc_inss
    sindicato = sb * perc_sindicato
    desconto = ir + inss + sindicato
    salarioLiquido = sb - desconto

    return f'Salario Bruto: R${sb:.2f}\n' \
           f'IR(11%): R${ir:.2f}\n' \
           f'INSS (8%): R${inss:.2f}\n' \
           f'Sindicato(5%): R${sindicato:.2f}\n' \
           f'Desconto: R${desconto:.2f}\n' \
           f'Salário Líquido R${salarioLiquido:.2f}'


salarioBruto = float(input('Informe o salario em R$'))
print(calcularSalarioLiquido(salarioBruto))


