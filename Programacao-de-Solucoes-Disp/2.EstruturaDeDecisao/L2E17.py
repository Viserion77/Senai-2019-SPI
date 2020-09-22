# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input('ano: '))

bissexto = False
if (ano % 4 == 0):
    bissexto = True
    if (ano % 100 == 0) and (ano % 400 != 0):
        bissexto = False

if (bissexto):
    print('BISSEXTO')
else:
    print('NAO BISSEXTO')