def convertTempCelsiusToFarenheit(celsius):
    return (celsius * 9 / 5) + 32
Celsius = float(input('Celsius: '))
print(convertTempCelsiusToFarenheit(Celsius))