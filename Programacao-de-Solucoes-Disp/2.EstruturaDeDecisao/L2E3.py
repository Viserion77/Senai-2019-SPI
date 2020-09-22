# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sex=input("Sexo (F, M): ")
if sex.lower()=="f":
    print("F - Feminino")
elif sex.lower()=="m":
    print("M - Masculino")
else:
    print("Sexo Inválido")