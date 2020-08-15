nome: str
valorHora: float
horasTrabalhadas: float
pagamento: float

nome = str(input('Nome: '))
valorHora = float(input('Valor por hora R$'))
horasTrabalhadas = float(input('Horas trabalhadas: '))

pagamento = valorHora * horasTrabalhadas

print(f'O pagamento para {nome} deve ser R${pagamento:.2f}')