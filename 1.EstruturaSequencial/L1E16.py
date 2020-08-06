# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
def calcular_preco_quantidade_tinta(metros):
    quantidade = metros*3
    quantidade /= 18
    if quantidade > int(quantidade):
        quantidade = int(quantidade)+1
    preco = quantidade*80
    return quantidade, preco
metros_quadrados = float(input("Metros quadrados: "))
quantidade, preco=calcular_preco_quantidade_tinta(metros_quadrados)

print("Usara " + str(quantidade)+" latas no valor de "+ str(preco))
