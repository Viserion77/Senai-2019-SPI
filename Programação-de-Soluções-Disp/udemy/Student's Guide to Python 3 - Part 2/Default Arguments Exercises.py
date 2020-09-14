# Here are some exercises to try:

# 1. Define a function printname() that takes in single parameter name that defaults to the string "Bob" and then returns a statement "My name is " + name
def printname(name = "Bob"):
    return "My name is " + name

# 2. Define a variable username that takes in an input of the user's name.
username = input("User name ai: ")

# 3. If username receives a value, print the printname() of username. (To check if a variable has a value, use if variable:)
if username:
    print(printname(username))

# 4. If it doesn't contain a value, print the function call without any parameters.
else:
    print(printname())

# 5. Run the program once inputting your name, and once just pressing enter to avoid putting any value. Does it default to the default parameter?
# ?

# Solution:
# Ty, for nothing

# def printname(name = "Bob"):
#   return "My name is " + name
#  
# username = input("Enter name ")
#  
# if username:
#   print(printname(var))
# else:
#   print(printname())
