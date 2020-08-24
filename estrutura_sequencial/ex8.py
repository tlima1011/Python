def informarSalario(vh, ht):
    return vh * ht


vh = float(input('Ganha por hora R$'))
ht = float(input('Hora trabalhadas: '))
print(f'Valor do salario R${informarSalario(vh,ht):.2f}')