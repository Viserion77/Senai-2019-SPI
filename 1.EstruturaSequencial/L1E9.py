# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
def convert_temp_farenheit_to_celsius(farenheit):
    return 5 * ((farenheit-32) / 9)
farenheit = float(input('farenheit: '))
print(convert_temp_farenheit_to_celsius(farenheit))