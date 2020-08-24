def validarDados(u, s):
    while u == s:
        print('Usuário e senha não pode ser iguais, informe novamente: ')
        u = str(input('Informe o usuário: ').strip().upper())
        s = str(input('Informe a senha: ').strip().upper())
    return 'Dados Válidos'


usuario = str(input('Informe o usuário: ').strip().upper())
senha = str(input('Informe a senha: ').strip().upper())
print(validarDados(usuario, senha))
"""Faça um programa que leia um nome de usuário e a sua senha e não
aceite a senha igual ao nome do usuário, mostrando uma mensagem
de erro e voltando a pedir as informações."""
