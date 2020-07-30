# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
def calcSalary(pricePerHour, HoursMonth):
    return pricePerHour * HoursMonth
pricePerHour = float(input('Valor/hora: '))
HoursMonth = float(input('Horas/Mes: '))
print(calcSalary(pricePerHour, HoursMonth))