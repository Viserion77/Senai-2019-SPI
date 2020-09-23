# Faça um Programa que leia três números e mostre o maior deles.
  
num1 = int(input('numero1: '))
num2 = int(input('numero2: '))
num3 = int(input('numero3: '))

if (num1 == num2) and (num1 == num3):
    print('\'-\'')
elif (num1 > num2) and (num1 > num3):
    print(num1)
elif (num2 > num3):
    print(num2)
else:
    print(num3)