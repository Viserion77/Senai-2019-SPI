# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

termo = 0
while (termo <= 0):
    termo = int(input('Voce quer o fatorial de qual termo: '))
    if (termo <= 0):
        print('O termo deve ser positivo!')

fatorial = 1
print('Fatorial de ' % termo,)
print('!%d = ' % termo,)
for i in reversed(range(2, termo + 1)):
    print('%d * ' % i,)
    fatorial *= i

print('1 = %d' % fatorial)
