n: int;

n = int(input('Quantos alunos serao digitados? '))

nomes: [str] = [0 for x in range(n)]
notas1 : [float] = [0 for x in range(n)]
notas2 : [float] = [0 for x in range(n)]
medias : [float] = [0 for x in range(n)]

for i in range(0, n):
    print(f'Digite nome, primeira e segunda nota do {i + 1}º aluno:')
    nomes[i] = input()
    notas1[i] = float(input())
    notas2[i] = float(input())
    medias[i] = (notas1[i] + notas2[i]) / 2.0

print('Alunos aprovados:')
for i in range(0, n):
    if medias[i] >= 6:
        print(f'{nomes[i]}')
