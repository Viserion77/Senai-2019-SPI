# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

somaVeiculos = 0
somaAcidentes = 0
somaAcidentesMenos2Mil = 0
totalCidadesMenos2Mil = 0

for i in range(0, 5):
    codigo = int(input('Informe o codigo da cidade: '))
    veiculos = int(input('Informe o numero de veiculos de passeio: '))
    acidentes = int(input('Informe a quantidade de acidentes em 1999: '))

    indiceAcidentes = acidentes / float(veiculos)
    somaVeiculos += veiculos

    if ('maisAcidentes' not in vars()) or (indiceAcidentes > maisAcidentes):
        maisAcidentes = indiceAcidentes
        codigoMaisAcidentes = codigo
    if ('menosAcidentes' not in vars()) or (indiceAcidentes < menosAcidentes):
        menosAcidentes = indiceAcidentes
        codigoMenosAcidentes = codigo

    if (veiculos < 2000):
        somaAcidentesMenos2Mil += acidentes
        totalCidadesMenos2Mil += 1

print('O cidade com maior indice de acidentes eh %i com %.2f',
      codigoMaisAcidentes, maisAcidentes)
print('O cidade com menor indice de acidentes eh %i com %.2f',
      codigoMenosAcidentes, menosAcidentes)
print('A media de veiculos nas cidades eh %.2f' % (somaVeiculos / 5.0))
print('A media de acidentes de transito nas cidades com menos de 2k veiculos eh %.2f',
      (somaAcidentesMenos2Mil / float(totalCidadesMenos2Mil)))
