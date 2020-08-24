def formarcaoTriangulo(r1, r2, r3):
  resultado: str
  if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
      resultado = 'Forma um triangulo '
      if r1 == r2 and r2 == r3:
          resultado += 'Equilátero'
      elif r1 != r2 and r2 != r3:
          resultado += 'Escaleno'
      else:
          resultado += 'Isósceles'
  else:
      resultado = 'Não forma um triangulo'
  return resultado


r1 = float(input('Informe a reta 1: '))
r2 = float(input('Informe a reta 2: '))
r3 = float(input('Informe a reta 3: '))
print(formarcaoTriangulo(r1, r2, r3))

