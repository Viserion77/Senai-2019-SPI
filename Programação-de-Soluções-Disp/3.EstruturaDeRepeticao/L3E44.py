# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

print('URNA ELETRONICA')
print('1 - Joao')
print('2 - Jose')
print('3 - Jaco')
print('4 - Jobe')
print('5 - Voto Nulo')
print('6 - Voto em Branco')

opcao1 = opcao2 = opcao3 = opcao4 = opcao5 = opcao6 = 0
totalVotos = 0
codigo = 1
while (codigo >= 1 and codigo <= 6):
    codigo = int(input('Informe a opcao ou zero para encerrar: '))
    if (codigo >= 1 and codigo <= 6):
        if (codigo == 1):
            opcao1 += 1
        elif (codigo == 2):
            opcao2 += 1
        elif (codigo == 3):
            opcao3 += 1
        elif (codigo == 4):
            opcao4 += 1
        elif (codigo == 5):
            opcao5 += 1
        elif (codigo == 6):
            opcao6 += 1
        totalVotos += 1

print('RESULTADO:')
print('1 - Joao - %d votos' % (opcao1))
print('2 - Jose - %d votos' % (opcao2))
print('3 - Jaco - %d votos' % (opcao3))
print('4 - Jobe - %d votos' % (opcao4))
print('5 - %d votos nulos' % (opcao5))
print('6 - %d votos em branco' % (opcao6))
print('Percentual de votos nulos: %.2f%%' % (opcao5 / float(totalVotos) * 100))
print('Percentual de votos em branco: %.2f%%',
      (opcao6 / float(totalVotos) * 100))
