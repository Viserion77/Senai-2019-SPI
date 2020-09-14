# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
for i in range(0, 5):
    numero = int(input('numero: '))
    soma += numero

print('A soma dos numeros digitados eh', soma)
print('A media dos numeros digitados eh', (soma / 5.0))
