# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
def calcular_preco_quantidade_tinta(metros, litro_area, litro_recipiente, preco_recipiente):
    quantidade = metros*litro_area*1.1

    recipiente_min = int(quantidade / litro_recipiente)

    quantidade /= litro_recipiente

    if quantidade > int(quantidade):
        quantidade = int(quantidade)+1

    preco = quantidade*preco_recipiente
    return quantidade, preco, recipiente_min


metros_quadrados = 3+0.6  # float(input("Metros quadrados: "))
quantidade_latas, preco_latas, min_latas = calcular_preco_quantidade_tinta(
    metros_quadrados, 6, 18, 80)
quantidade_galoes, preco_galoes, min_galoes = calcular_preco_quantidade_tinta(
    metros_quadrados, 6, 3.6, 25)


min_galoes = int(((metros_quadrados/6) - min_latas) / 3.6)
if min_galoes > int(min_galoes):
    min_galoes = int(min_galoes)+1

print("Usara " + str(quantidade_latas) +
      " latas no valor de " + str(preco_latas))
print("Usara " + str(quantidade_galoes) +
      " galoes no valor de " + str(preco_galoes))
print("Ou " + str(min_latas)+" latas mais " + str(min_galoes)+" galoes")
