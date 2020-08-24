def informarSexo(s):
    sexo = s.upper()
    if sexo == 'M':
        return 'Masculino'
    elif sexo == 'F':
        return 'Feminino'
    else:
        return 'Inválido'


sexo = str(input('Informe o sexo [M]/[F]: ').upper()[0])
print(f'O sexo é {informarSexo(sexo)}')