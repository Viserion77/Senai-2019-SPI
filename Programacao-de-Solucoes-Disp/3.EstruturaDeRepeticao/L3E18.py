# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

quantidade = 0
while (quantidade <= 0):
    quantidade = int(input('Voce quer informar quantos numeros: '))
    if (quantidade <= 0):
        print('Quantidade deve ser positiva!')

soma = 0
for i in range(0, quantidade):
    numero = 1001
    while (numero > 1000):
        numero = int(input('Informe um numero: '))
        if (numero > 1000):
            print('O numero deve ser menor ou igual a 1000!')
    if ('maior' not in vars()) or (numero > maior):
        maior = numero

    if ('menor' not in vars()) or (numero < menor):
        menor = numero

    soma += numero

print('Menor:', menor)
print('Maior:', maior)
print('Soma:', soma)