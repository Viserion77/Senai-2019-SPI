# Here are some exercises to try:

# 1. Assign a variable to the string: "Lewis Carroll: Adam in Wonderland".
variable = "Lewis Carroll: Adam in Wonderland"

# 2. There's something wrong with this string... but where is it....? Print the index that the word Adam begins on in a statement "The error is on index _". Use fstrings to make this easier!
error = variable.find("Adam")

# 3. Let's fix the mistake. Replace the word Adam with Alice.
print(f"The error is on index {error}")

# 4. Print a statement that says "We fixed the string: Lewis Carroll: Alice in Wonderland". Use fstrings.
variable = variable.replace("Adam", "Alice")
print(f"We fixed the string: {variable}")

# Solution:

# book = "Lewis Carroll: Adam in Wonderland"
# error = book.find("Adam")
# print(f"The error is on index {error}")
# book = book.replace("Adam", "Alice")
# print(f"We fixed the string: {book}")