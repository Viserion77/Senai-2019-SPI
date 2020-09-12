# Here are some exercises you can try:

# 1. Define a function greeting() to print a statement with your name and age. Then call your function.
def greeting():
    print("Jeferson Alves, 19 Anos")
greeting()

# 2. Put another print statement in your function that says: Goodbye!
def statement():
    print("Goodbye!")
statement()

# 3. Call your function and see what it prints.
statement()

# 4. Remove the indent on the print statement with "Goodbye!" and remove your function call. Then run your program to see what happens.
# No!

# 5. Remove that print statement entirely and write a new function farewell() that prints: Goodbye! Have a great day!
def farewell():
    print("Goodbye! Have a great day")

# Solution:

# Whitespace matters, so if the print statement is not indented, it is not considered part of your function. Therefore, when you call your function it will not run with that print statement. And even if you don't call the function itself, that print statement will still run because it is not part of the function's definition.