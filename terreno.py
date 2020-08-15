largura: float
comprimento: float
valor: float
area: float
preco: float

largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
valor = float(input('Digite o valor do metro quadrado: '))# 200.00

area = largura * comprimento
preco = area * valor

print(f'Area do terreno = {area:.2f}') #300.00
print(f'Preco do terreno = R${preco:.2f}') #60000.00