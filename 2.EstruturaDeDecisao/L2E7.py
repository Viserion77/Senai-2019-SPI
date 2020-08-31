# Faça um Programa que leia três números e mostre o maior e o menor deles.
  
num1 = int(input('numero1: '))
num2 = int(input('numero2: '))
num3 = int(input('numero3: '))

if (num1 == num2) and (num1 == num3):
    print( 'bAIT')
else:
    if (num1 > num2) and (num1 > num3):
        print( 'maior', num1)
    elif (num2 > num3):
        print( 'maior', num2)
    else:
        print( 'maior', num3)

    if (num1 < num2) and (num1 < num3):
        print( 'menor', num1)
    elif (num2 < num3):
        print( 'menor', num2)
    else:
        print( 'menor', num3)