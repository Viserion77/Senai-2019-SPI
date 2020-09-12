# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
# Entrada de dados
totalMorangos =\
    float(input('morangos: '))
totalMacas =\
    float(input('macas: '))

# Calcula o valor bruto
if (totalMorangos <= 5):
    valorMorangos = totalMorangos * 2.5
else:
    valorMorangos = totalMorangos * 2.2

if (totalMacas <= 5):
    valorMacas = totalMacas * 1.8
else:
    valorMacas = totalMacas * 1.5

valorBruto = valorMorangos + valorMacas

# Verifica os descontos
if ((totalMorangos + totalMacas) >= 8) or (valorBruto >= 25):
    valorBruto = valorBruto * 0.9

# Imprime o resultado
print('pagar: ', valorBruto)