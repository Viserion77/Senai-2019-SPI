# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.
valor = float(input())

opcao = input('1 - Par ou Impar\n2 - Positivo ou Negativo\n3 - Inteiro ou Decimal\nopcao: ')

if (opcao == '1'):
    if (valor % 2 == 0):
        print('par')
    else:
        print('impar')
elif (opcao == '2'):
    if (valor < 0):
        print('negativo')
    elif (valor > 0):
        print('positivo')
    else:
        print('igual a zero')
elif (opcao == '3'):
    if (valor == int(valor)):
        print('inteiro')
    else:
        print('decimal')
else:
    print('Opcao Invalida')