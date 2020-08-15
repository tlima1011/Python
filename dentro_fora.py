n: int; numeros: int; dentro: int; fora: int;
dentro = fora = 0

n = int(input('Quantos numeros voce vai digitar? '))#5
for i in range(1, n+1):
    numeros = int(input(f'Digite {i}º numero: '))
    if numeros >= 10 and numeros <= 20:
        dentro += 1
    else:
        fora += 1

print(f'{dentro} DENTRO')
print(f'{fora} FORA')