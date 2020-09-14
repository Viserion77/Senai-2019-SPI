# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
def calc_area_by_radius(radius):
    return (radius ** 2) * 3.141592653589793
radius = float(input('Raio :'))
print(calc_area_by_radius(radius))