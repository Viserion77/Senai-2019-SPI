# Here are some exercises to try:

# 1. Try defining a global variable globe and set it equal to your name.
globe="to your name"

# 2. Define a function friends() that takes in name as a parameter, and returns a statement globe + " and " + name + " are friends."
def friends(name = "nobody"):
    return "a statement "+globe+" + \" and \" + "+name+" + \" are friends.\""

# 3. Call your function on "Bob" and print it. Can it use globe in the function definition?
print(friends("\"bob\""))

# 4. Define a variable local inside the definition of your function that is also equal to your name. Replace the variable global in your return statement with local.
# wtf
def your_function(name):
    loval_variable=name
    return loval_variable

globe=your_function("Ç?")

# 5. Call your function on "Bob" and print it. Then print the value of local. Can you see the value?
print(your_function("blu, com b de bobo, l de lixo e u de ..."))

# Solution:

# globe = "Amy"
# def friends(name):
#   return globe + " and " + name + " are friends."
#  
# print(friends(globe))
# def friends(name):
#   local = "Amy"
#   return local + " and " + name + " are friends."
#  
# print(friends("Bob"))
# print(local)
# Printing local throws an error because it is a local variable. This means that only code inside where it is defined has access to local, so anywhere inside friends() we would be able to print the value of local, however, once we step outside, we lose access to it. globe is a global variable so we can use it anywhere we want.