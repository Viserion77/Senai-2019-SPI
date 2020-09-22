# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = senha = ''
while (usuario == senha):
    usuario = input('usuario: ')
    senha = input('senha: ')
    if (usuario == senha):
        print('A senha nao pode ser igual ao nome do usuario')
