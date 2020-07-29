def calcSalary(pricePerHour, HoursMonth):
    return pricePerHour * HoursMonth
pricePerHour = float(input('Valor/hora: '))
HoursMonth = float(input('Horas/Mes: '))
print(calcSalary(pricePerHour, HoursMonth))