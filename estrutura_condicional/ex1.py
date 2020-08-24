def informarMaior(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


#Faça um Programa que peça dois números e imprima o maior deles.
numero1 = int(input('Informe o primeiro numero: '))
numero2 = int(input('Informe o primeiro numero: '))
print(f'O maior número é {informarMaior(numero1, numero2)}')