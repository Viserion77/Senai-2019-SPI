# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input('numero1: '))
num2 = int(input('numero2: '))
num3 = int(input('numero3: '))

list=[num1,num2,num3]
list.sort(reverse=True)
print(list)