# 1. Try defining a variable with operations, eg: num = 5+5
num = 5+5  # Easy

# 2. Try using exponents in defining a variable
exponenten = 2**2

# 3. Print a mathematical expression using different operations including modulo. Where does modulo fit in the order of operations?
print(1+2-3*4/5 % 6)

# 4. Print an expression using only variables
print(num*num)

# 5. Define a variable using only other variables
ber = 0*666
number = num+ber

# Solution for 3

# Modulo has the same precedence as division and multiplication, meaning that division, multiplication, and modulo will all be calculated at the same time in a right to left fashion. 3**2+3/3%6 will first calculate 3**2 = 9, then 3/3 = 1, then 1%6 = 1, then 9+1 = 10.

# Solution for 4

#     num1 = 4
#     num2 = 5
#     num3 = 2
#     print(num1/num3+num2)

# Solution for 5

# `num4 = num1/num3`
