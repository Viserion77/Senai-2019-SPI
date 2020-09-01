# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
num = int(input('Informe um numero inteiro: '))

centenas = num / 100
dezenas = (num - (centenas * 100)) / 10
unidades = (num - (centenas * 100) - (dezenas * 10))

saida = ''
if (centenas > 0):
    saida = saida + str(centenas)
    if (centenas > 1):
        saida = saida + ' centenas '
    else:
        saida = saida + ' centena '

if (dezenas > 0):
    if (unidades == 0) and (centenas != 0):
        saida = saida + 'e '
    saida = saida + str(dezenas)
    if (dezenas > 1):
        saida = saida + ' dezenas '
    else:
        saida = saida + ' dezena '

if (unidades > 0):
    if (centenas != 0) or (dezenas != 0):
        saida = saida + 'e '
    saida = saida + str(unidades)
    if (unidades > 1):
        saida = saida + ' unidades'
    else:
        saida = saida + ' unidade'

print(saida)