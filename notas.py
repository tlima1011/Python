nota1: float;  nota2: float;  notaFinal: float


nota1 = float(input('Digite a primeira nota: ')) #45.5
nota2 = float(input('Digite a segunda nota: ')) #31.3
notaFinal = nota1 + nota2

print(f'NOTA FINAL = {notaFinal}')#76.8
if notaFinal < 60:
    print('REPROVADO')