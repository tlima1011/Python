n: int; nomeVelho: str; idadeVelho: int;

n = int(input('Quantas pessoas voce vai digitar? '))

nomes: [str] = [0 for x in range(n)]
idades: [int] = [0 for x in range(n)]

for i in range(0, n):
    print(f'Dados da {i + 1}ª pessoa:')
    nomes[i] = str(input('Nome: '))
    idades[i] = int(input('Idade: '))

nomeVelho = nomes[0]
idadeVelho = idades[0]

for i in range(1,n):
    if idades[i] > idadeVelho:
        nomeVelho = nomes[i]
        idadeVelho = idades[i]

print(f'PESSOA MAIS VELHA: {nomeVelho} com {idadeVelho} anos.')
