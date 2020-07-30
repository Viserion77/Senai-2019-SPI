# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
def calcAreaByRadius(radius):
    return (radius ** 2) * 3.141592653589793
radius = float(input('Raio :'))
print(calcAreaByRadius(radius))