# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
print('Programa Detetive')
print('Responda as perguntas abaixo com S/N')

telefonou = input('Voce telefonou para a vitima? ').upper()
localCrime = input('Voce esteve no local do crime? ').upper()
moraPerto = input('Voce mora perto da vitima? ').upper()
devia = input('Voce devia para a vitima? ').upper()
trabalhou = input('Voce trabalhou para a vitima? ').upper()

classificacao = 0

if (telefonou == 'S'):
    classificacao += 1

if (localCrime == 'S'):
    classificacao += 1

if (moraPerto == 'S'):
    classificacao += 1

if (devia == 'S'):
    classificacao += 1

if (trabalhou == 'S'):
    classificacao += 1

if (classificacao < 2):
    print('Inocente')
elif (classificacao == 2):
    print('Suspeito')
elif (classificacao <= 4):
    print('Cumplice')
else:
    print('Assassino')