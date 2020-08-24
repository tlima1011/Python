def informarDados(n, i, s, se, ec):
    return f'Dados do usuário: \n' \
           f'Nome: {n.capitalize()}\n' \
           f'Idade: {i} anos.\n' \
           f'Salário: R$ {s:.2f}\n' \
           f'Sexo: [{se}]\n' \
           f'Estado Civil: [{ec}]'

nome: str
nome = str(input('Informe o nome: ').strip())
while len(nome) < 3:
    nome = str(input('Inválido, informe nome com mais de 3 caracteres: ').strip())

idade = int(input('Informe a idade: '))
while 0 < idade > 150:
    idade = int(input('Inválido, informe idade entre 0 e 150: '))

salario = float(input('Informe o salário em R$'))
while salario < 0:
    salario = float(input('Inválido, informe salário maior que 0: '))

sexo = str(input('Informe o Sexo [M]/[F]: ').strip().upper()[0])
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Inválido, Informe o Sexo [M]/[F]: ').strip().upper()[0])

estadoCivil = str(input('Informe o estado civil [S] / [C] / [V] / [D]: ').strip().upper()[0])
while estadoCivil != 'S' and estadoCivil != 'C' and estadoCivil != 'V' and estadoCivil != 'D':
    estadoCivil = str(input('Inválido, Informe o estado civil [S] / [C] / [V] / [D]: ').strip().upper()[0])

print(informarDados(nome, idade, salario, sexo, estadoCivil))
