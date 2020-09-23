#Here are some exercises you can try:

#1. Define a function times3plus2() that takes in a single parameter num and prints the result of that num times 3, plus 2.
def times3plus2(single_parameter):
    print(single_parameter*3+2)


#2. Call it on numbers 1, 2, and 3.
times3plus2(1)
times3plus2(2)
times3plus2(3)

#3. Define a variable and set it equal to 6.
variable=6

#4. Call your function on the variable.
times3plus2(variable)

#5. Define another function twotimespowerof() that takes in two parameters, base and exponent , and prints the result of 2 times (the base raised to the power of exponent).
def twotimespowerof(base,exponent):
    print(2*(base**exponent))

#6. Define two variables that take in the user's input, and ask for a base and an exponent.
variable1 = int(input("variable 1: "))
variables2 = int(input("variable 2: "))

#7. Call your twotimespowerof()  function on those two variables.
twotimespowerof(variable1,variables2)

#Solution:

#def times3plus2(num):
#    print(3*num+2)
#times3plus2(1)
#times3plus2(2)
#times3plus2(3)
#test = 6
#times3plus2(test)
# 
#def twotimespowerof(base, exponent):
#    print(2*(base**exponent))
# 
#userbase = input("Input a base ")
#userexponent = input("Input an exponent ")
#twotimespowerof(int(userbase), int(userexponent))