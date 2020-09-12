# Here are some exercises to try:

# 1. Define a function luckify()  that takes in a string as a parameter and returns that string with "777" at the end of the string.
def luckify(string):
    return string+"777"

# 2. Call the function on your name, and print that.
print(luckify("Faz Sol, ") + ":D")

# 3. Set a variable luckyname equal to the function call on your name.
luckyname=luckify("luckify?")

# 4. Print the value of luckyname.
print(luckyname)

# 5. Call luckify() on luckyname, and set that equal to luckyname.
luckyname=luckify(luckyname)

# 6. Print the value of luckyname.
print(luckyname)

# Solution:

# def luckify(string)
#     return string + "777"
#  
# print(luckify("Joey"))
# luckyname = luckify("Joey")
# print(luckyname) 
# luckyname = luckify(luckyname)
# print(luckyname)
# The first two print statements print the exact same thing. The value that is stored in the function call luckify("Joey") is now being stored in luckyname. The advantage of using return is that now we can store that value and manipulate it.