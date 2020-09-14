# Altere o programa anterior para mostrar no final a soma dos números.

inicial = int(input('inicial: '))
final = inicial
while (final <= inicial):
    final = int(input('final: '))
    if (final <= inicial):
        print('O valor final deve ser maior que o valor final!')

soma = 0
for i in range(inicial, final + 1):
    soma += i
    print(i)

print(soma)
