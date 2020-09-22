# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

def retonaSeNumeroImpar(valor):
    resto=valor%2
    isImpar=0
    if (resto):
        isImpar=valor
    return isImpar

numero = input('numero: ')
print(str(retonaSeNumeroImpar(int(numero))))
