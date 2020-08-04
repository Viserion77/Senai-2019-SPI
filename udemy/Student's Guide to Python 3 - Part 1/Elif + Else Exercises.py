# 1. Set a variable equal to the user's input asking for their grade percentage.
variable = input("\"for their grade percentage\": ")

# 2. Use an if statement to check if their grade is greater than or equal to a 90%, and if so, print out a statement telling them that their grade is an A.
variable = int(variable) # "se eu soubesse" podia colocar isso no input mesmo.....
if variable>=90:
    print("grade is an A")

# 3. Repeat for letter grades B, C, and D, remembering to use elif
# creio eu que deva ir diminuindo de 10 em 10
elif variable>=80:
    print("grade is an B")
elif variable>=70:
    print("grade is an C")
elif variable>=60:
    print("grade is an D")

# 4. Use else to cover anything below a D, and classify it as an F.
else:
    print("grade is an F")

# 5. Run your program, and if done right, it should only print out 1 statement. Remember that order matters, so make sure to put your if statements in the order of A, B, C, D, and F.
# :D