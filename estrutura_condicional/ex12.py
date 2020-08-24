def calcularFolha(v,h):
    desconto: float; perc_inss: float; inss:float; perc_sindicato: float; sindicato: float; ir: float; perc_ir: float; fgts: float; perc_fgts: float
    sb = v * h
    perc_inss = 0.10
    perc_fgts = 0.11
    perc_sindicato = 0.03
    if sb <= 900:
        perc_ir = 0
    elif sb <= 1500:
        perc_ir = 0.05
    elif sb <= 2500:
        perc_ir = 0.10
    else:
        perc_ir = 0.20
    inss = perc_inss * sb
    ir = perc_ir * sb
    fgts = perc_fgts * sb
    desconto = ir+inss
    salario = sb - desconto

    return f'''Salário Bruto: ({h} * {v}): R${sb:.2f}
    IR({perc_ir * 100:.0f}%): R${ir:.2f}
    INSS({perc_inss * 100:.0f}%): R${inss:.2f}
    FGTS({perc_fgts * 100:.0f}%): R${fgts:.2f}
    Total de descontos: R${desconto:.2f}
    Salário Liquido: R${salario:.2f}'''


valorHora = float(input('Informe o valor por hora R$'))
horas = int(input('Informe a horas trabalhadas: '))
print(calcularFolha(valorHora,horas))

