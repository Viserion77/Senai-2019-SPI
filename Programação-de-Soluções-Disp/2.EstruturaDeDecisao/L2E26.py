# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
# Solicita informacoes
tipoCombustivel =\
    input('A/G').upper()
quantidadeLitros = float(input('quantidade: '))

# Define o valor e os descontos
if (tipoCombustivel == 'A'):
    valor = 1.9
    if (quantidadeLitros <= 20):
        desconto = 3
    else:
        desconto = 5
else:
    valor = 2.5
    if (quantidadeLitros <= 20):
        desconto = 4
    else:
        desconto = 6

# Calcula o total
totalPagar = (valor * quantidadeLitros) * ((100 - desconto) / 100.0)

print('Total: ', totalPagar)