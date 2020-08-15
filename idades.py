nome1: str; nome2: str
idade1: int; idade2: int

print('Dados da primeira pessoa:')
nome1 = input('Nome: ')
idade1 = int(input('Idade: '))# 19

print('Dados da segunda pessoa:')
nome2 = input('Nome: ')
idade2 = int(input('Idade: '))# 19

media = (idade1 + idade2) / 2

print(f'A idade média de {nome1} e {nome2} é de {media:.1f} anos.')
