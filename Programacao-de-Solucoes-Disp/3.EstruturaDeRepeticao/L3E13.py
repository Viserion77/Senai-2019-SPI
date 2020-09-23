# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input('base: '))
expoente = 0
while (expoente <= 0):
    expoente = int(input('expoente: '))
    if (expoente <= 0):
        print('O expoente deve ser positivo!')

potencia = 1
for i in range(1, expoente + 1):
    potencia *= base

print(base, 'elevada a', expoente, '=', potencia)
