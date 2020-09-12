# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

grade1 = float(input("Nota 1: "))
grade2 = float(input("Nota 2: "))
def student_status(media):
    if media>=7:
        if media==10:
            return "Aprovado com Distinção"
        else:
            return "Aprovado"
    else:
        return "Repovado"
print(student_status(((grade1+grade2)/2)))