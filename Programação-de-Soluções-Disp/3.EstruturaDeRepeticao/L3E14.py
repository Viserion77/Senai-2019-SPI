# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

print('Informe 10 numeros')
pares = 0
impares = 0
for i in range(1, 11):
    numero = int(input('Informe um numero: '))
    if (numero % 2 == 0):
        pares += 1
    else:
        impares += 1

print('Numeros pares:', pares)
print('Numeros impares:', impares)
