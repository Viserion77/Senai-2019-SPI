# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
termo = 0
while (termo <= 0):
    termo = int(input('termo: '))
    if (termo <= 0):
        print('deve ser positivo!')

primeiro = 0
print(primeiro)
segundo = 1
for i in range(1, termo):
    print(segundo)
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro
