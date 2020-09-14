# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#   Calcule e mostre o total do seu salário no referido mês,
#   sabendo-se que são descontados 11% para o Imposto de Renda,
#   8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#      salário bruto.
#      quanto pagou ao INSS.
#      quanto pagou ao sindicato.
#      o salário líquido.
#      calcule os descontos e o salário líquido, conforme a tabela abaixo:
#      + Salário Bruto : R$
#      - IR (11%) : R$
#      - INSS (8%) : R$
#      - Sindicato ( 5%) : R$
#      = Salário Liquido : R$
#      Obs.: Salário Bruto - Descontos = Salário Líquido.
how_muth_want = float(input("Quanto quer ganhar (Por hora)? : "))
how_muth_work = float(input("Quanto quer trabalhar (Em hora, por mes)? : "))
salario_bruto = how_muth_want*how_muth_work
quanto_pagou_ir = salario_bruto*0.11
quanto_pagou_ao_inss = salario_bruto*0.08
quanto_pagou_ao_sindicato = salario_bruto*0.05
o_salario_liquido = salario_bruto - \
    (quanto_pagou_ir+quanto_pagou_ao_inss+quanto_pagou_ao_sindicato)
print("salario_bruto = "+str(salario_bruto))
print("quanto_pagou_ir = "+str(quanto_pagou_ir))
print("quanto_pagou_ao_inss = "+str(quanto_pagou_ao_inss))
print("quanto_pagou_ao_sindicato = "+str(quanto_pagou_ao_sindicato))
print("o_salario_liquido = "+str(o_salario_liquido))
