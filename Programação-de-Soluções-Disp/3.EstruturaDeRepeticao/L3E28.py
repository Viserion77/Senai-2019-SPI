# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quantidade = 0
while (quantidade <= 0):
    quantidade = int(input('Informe a quantidade de CDs: '))
    if (quantidade <= 0):
        print('A quandidade deve ser positiva!')

soma = 0
for i in range(0, quantidade):
    valor = -1
    while (valor < 0):
        valor = float(input('Informe o valor pago pelo CD: '))
        if (valor < 0):
            print('O valor deve ser maior ou igual a 0')
    soma += valor

media = soma / float(quantidade)

print('Quantidade de CDs:', quantidade)
print('Media do valor dos CDs:', media)
