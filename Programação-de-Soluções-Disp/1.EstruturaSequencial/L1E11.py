# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a: o produto do dobro do primeiro com metade do segundo .
# b: a soma do triplo do primeiro com o terceiro.
# c: o terceiro elevado ao cubo.
intNumber1 = int(input('Numero inteiro 1: '))
intNumber2 = int(input('Numero inteiro 2: '))
realNumber = float(input('Numero real: '))
print(str((intNumber1*2)*(intNumber2/2)))
print(str((intNumber1*3)+realNumber))
print(str(realNumber**3))