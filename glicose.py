classificacao: str
glicose: float

glicose = float(input('Digite a medida da glicose: '))

if glicose <= 100:
    classificacao = 'Normal'
elif glicose <= 140:
    classificacao = 'Elevado'
else:
    classificacao = 'Diabetes'
print(f'Classificacao: {classificacao}')

'''Classificacao: normal
Exemplo 2:
Digite a medida da glicose: 140.0
Classificacao: elevado
Exemplo 3:
Digite a medida da glicose: 143.2
Classificacao: diabetes'''