# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# Validacao do nome
nome = ''
while (len(nome) <= 3):
    nome = input('um nome: ')
    if (len(nome) <= 3):
        print('O nome deve ter mais de tres letras!')

# Validacao da idade
idade = -1
while (idade < 0) or (idade > 150):
    idade = int(input('a idade: '))
    if (idade < 0) or (idade > 150):
        print('Idade deve estar entre 0 e 150')

# Validacao do salario
salario = 0
while (salario <= 0):
    salario = int(input('o salario: '))
    if (salario <= 0):
        print('O salario deve ser maior que zero')

# Valida o sexo
sexo = ''
while (sexo != 'F') and (sexo != 'M'):
    sexo = input('o sexo: ').upper()
    if (sexo != 'F') and (sexo != 'M'):
        print('O sexo deve ser infomado como M (masculino) ou F (feminino)')

# Valida o estado civil
estado_civil = 'A'
while ('SCVD'.find(estado_civil) < 0):
    estado_civil = input('o estado civil: ').upper()
    if ('SCVD'.find(estado_civil) < 0):
        print('Estado civil deve ser informado como S (solteiro), C (casado), V (viuvo) ou D (divorciado)')