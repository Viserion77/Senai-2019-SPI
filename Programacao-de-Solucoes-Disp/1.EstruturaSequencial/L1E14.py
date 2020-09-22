# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso
# (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa
# o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
kgs_estabelecidos_sp = 50.0
multa_kg_ecedente = 4.0
kgs_adquirido = float(input("kgs adiquerido: "))
if kgs_adquirido>kgs_estabelecidos_sp:
    print("Pescado " + str(kgs_adquirido-kgs_estabelecidos_sp) + " a mais que o  estabelecido!")
    print("Multa de: R$"+str((kgs_adquirido-kgs_estabelecidos_sp)*multa_kg_ecedente))
else:
    print("Pescado " + str(kgs_estabelecidos_sp-kgs_adquirido) + " a menos que o  estabelecido!")