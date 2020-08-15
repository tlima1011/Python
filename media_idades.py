idade: int; media: float; soma: float
n: int

soma = 0
n = 0
print('Digite as idades:')
idade = int(input())
if idade < 0:
    print('IMPOSSIVEL CALCULAR')
    exit()
else:
    while idade >= 0:
        n += 1
        soma += idade
        idade = int(input())
media = soma / n
print(f'MEDIA = {media:.2f}')