def convertTempFarenheitToCelsius(farenheit):
    return 5 * ((farenheit-32) / 9)
farenheit = float(input('farenheit: '))
print(convertTempFarenheitToCelsius(farenheit))