def calcularMediaAlunos(n):
    alunos: int
    alunos = 0
    soma = 0
    media = 0
    for i in range(0, n):
        print(f'{i + 1}ª turma: ')
        alunos = int(input('Informe quantidade de alunos: '))
        while alunos > 40:
            alunos = int(input('Inválido, não pode ser maior que 40: '))
        soma += alunos
    media = soma / n
    return f'Média de alunos por turma {media:.1f}'


"""Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para
cada turma. As turmas não podem ter mais de 40 alunos."""
n = int(input('Informe a quantidade de turmas: '))
print(calcularMediaAlunos(n))


