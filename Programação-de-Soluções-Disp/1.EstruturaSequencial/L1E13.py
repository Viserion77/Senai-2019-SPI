# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
height = float(input("Altura: "))
print("Men " + str((72.7*height) - 58))
print("Woman " + str((62.1*height) - 44.7))