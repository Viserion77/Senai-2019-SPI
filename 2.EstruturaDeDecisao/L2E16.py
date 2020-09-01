# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math

valorA = float(input('Calculo de equacao de Segundo Grau\na : '))
valorB = float(input('b : '))
valorC = float(input('c : '))

if (valorA == 0):
    print('Os valores nao formam uma equacao de segundo grau')
else:
    delta = math.pow(valorB, 2) - (4 * valorA * valorC)

    if (delta < 0):
        print('A equacao nao possui valores reais.')
    elif (delta == 0):
        print('A equacao possui apenas uma raiz')
        raiz = -(valorB) / (2 * valorA)
        print('Raiz:', raiz)
    else:
        print('A equacao possui duas raizes')
        raiz1 = (-(valorB) + math.sqrt(delta)) / (2 * valorA)
        raiz2 = (-(valorB) - math.sqrt(delta)) / (2 * valorA)
        print('Raiz 1:', raiz1)
        print('Raiz 2:', raiz2)