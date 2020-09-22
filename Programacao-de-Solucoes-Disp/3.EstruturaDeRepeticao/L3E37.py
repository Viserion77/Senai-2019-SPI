# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

codigo = -1
totalClientes = 0
somaAlturas = 0.0
somaPesos = 0.0
while (codigo != 0):
    codigo = int(input('Informe o codigo do cliente: '))
    if (codigo != 0):
        altura = float(input('Informe a altura do cliente: '))
        peso = float(input('Informe o peso do cliente:'))
        totalClientes += 1
        somaAlturas += altura
        somaPesos += peso
        if ('maisAlto' not in vars()) or (altura > maisAlto):
            maisAlto = altura
            codigoMaisAlto = codigo
        if ('maisBaixo' not in vars()) or (altura < maisBaixo):
            maisBaixo = altura
            codigoMaisBaixo = codigo
        if ('maisGordo' not in vars()) or (peso > maisGordo):
            maisGordo = peso
            codigoMaisGordo = codigo
        if ('maisMagro' not in vars()) or (peso < maisMagro):
            maisMagro = peso
            codigoMaisMagro = codigo

print('O cliente mais alto eh o de codigo %i com %f' %
      codigoMaisAlto, maisAlto)
print('O cliente mais baixo eh o de codigo %i com %f' %
      codigoMaisBaixo, maisBaixo)
print('O cliente mais magro eh o de codigo %i com %f' %
      codigoMaisMagro, maisMagro)
print('O cliente mais gordo eh o de codigo %i com %f' %
      codigoMaisGordo, maisGordo)

print('Media da altura dos clientes: %.2f' %
      somaAlturas / float(totalClientes))
print('Media dos pesos dos clientes: %.2f' %
      somaPesos / float(totalClientes))
