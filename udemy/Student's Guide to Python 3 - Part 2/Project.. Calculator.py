# In this project, we will make an interactive calculator that takes in the user's input.

# 1. You are making a calculator app! Print some lines welcoming the user to the app.

# 2. We will need to define some functions. Define an add, subtract, multiply, and divide function that will take two parameters and do that operation to them, and return the result.
def add(a=0,b=0):
    return a+b

def subtract(a=0,b=0):
    return a-b

def multiply(a=0,b=0):
    return a*b
    
def divide(a=0,b=0):
    if not b==0:
        return a*b
    else:
        return 0

# 3. Make another function exponent that takes in a base and a power. Return the result of the base to that power.
def exponent(a,b):
    return a**b

# 4. Make another function remainder_division that takes in two numbers. The function should then return the result - not in decimal form - but with the answer and a remainder.
def remainder_division(a,b):
    return 

# 4a. In order to create such a function, we will need to use import math. What this does is it allows us to use functions that have been made by other people so that we don't need to create them ourselves. We're going to be using the math.floor() function that rounds a number down to its ones place, getting rid of all the decimal places.

# 4b. Inside your function, define a local variable answer and set it equal to the dividend divided by the divisor. Then, math.floor(answer). Define another local variable remainder and set it equal to the dividend modulo (%) the divisor.

# 4c. Finally, return the answer and the remainder using string concatenation in the format "A remainder B". Don't forget to use the str() method to concatenate numbers with strings.

# 5. Define our last function square_root that takes in a number and returns the square root of that number. We will need to use math.sqrt() in order to do this.

# 6. It's time to ask the user for their input! Define a variable that takes in the user input. When taking the input, display a string such as:

# What function would you like to use?

# 1. Add

# 2. Subtract

# 3. Multiply

# 4. Divide

# etc...

# 7. Their input should be a number, so define a matching number of if statements to account for each function, checking if the input is equal to "1" or etc. Make sure the number is a string because the inputed value is automatically a string. Then, inside each if statement, define the corresponding number of local variables to how many inputs the function requires. For example, if the user chose square root, I would only define one local variable and ask for the input. If they chose exponent, I would define two local variables and set it equal to the user's inputed base and power. Call the function on the variables and print the result. Make sure when you call your function on the variables that you use the int() method because the input variables are automatically strings.

# 8. Test your program! Does it work? Ask your friends and family to test it out, and feel free to improve it and customize it!