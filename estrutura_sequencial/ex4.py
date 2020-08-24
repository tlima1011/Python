def mostrarMedia(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 2.0


nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
nota3 = float(input('Informe a nota 3: '))
nota4 = float(input('Informe a nota 4: '))
print(f'Media {mostrarMedia(nota1,nota2,nota3,nota4):.1f}')