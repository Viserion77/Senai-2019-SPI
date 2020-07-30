#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
def convert_temp_celsius_to_farenheit(celsius):
    return (celsius * 9 / 5) + 32
Celsius = float(input('Celsius: '))
print(convert_temp_celsius_to_farenheit(Celsius))