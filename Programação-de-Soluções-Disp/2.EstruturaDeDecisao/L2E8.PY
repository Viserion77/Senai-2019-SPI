# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco1 = int(input('primeiro '))
preco2 = int(input('segundo '))
preco3 = int(input('terceiro '))

if (preco1 == preco2) and (preco1 == preco3):
    print('IGUAIS.')
elif (preco1 < preco2) and (preco1 < preco3):
    print('primeiro')
elif (preco2 < preco3):
    print('segundo')
else:
    print('terceiro')