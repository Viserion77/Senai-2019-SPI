#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
def convertTempCelsiusToFarenheit(celsius):
    return (celsius * 9 / 5) + 32
Celsius = float(input('Celsius: '))
print(convertTempCelsiusToFarenheit(Celsius))