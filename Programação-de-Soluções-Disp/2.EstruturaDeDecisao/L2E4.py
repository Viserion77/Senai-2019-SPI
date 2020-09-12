# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letter=input("Letra: ")
vogais={"a","e","i","o","u"}
if len(letter)>1:
    print("Não é uma letra")
else:
    if letter in vogais:
        print("Vogal")
    else:
        print("Consoante")