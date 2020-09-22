# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67

divida = float(input('Informe o valor da divida: '))

print('Valor da divida\tValor dos Juros\tQuantidade de Parcelas\tValor da Parcela juros = 0')
for i in [1, 3, 6, 9, 12]:
    valorJuros = (divida * (juros / 100.0))
    valorDivida = divida + valorJuros
    valorParcela = valorDivida / float(i)
    print('R$ %.2f\tR$ %.2f\t%i\tR$ %.2f',
          (valorDivida, valorJuros, i, valorParcela))
    if (i == 1):
        juros = 10
    else:
        juros += 5
