# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
def convertTempFarenheitToCelsius(farenheit):
    return 5 * ((farenheit-32) / 9)
farenheit = float(input('farenheit: '))
print(convertTempFarenheitToCelsius(farenheit))