# 1. Try asking for the user's name and age, and use string concatenation to print out a statement saying something along the lines of: Hi, my name is ____ and I'm ____ years old.
user_name = input("say your name: ")
user_age = input("keyar your age: ")
print("Hi, my name is "+user_name+" and I'm "+user_age+" years old")

# 2. To make sure they aren't impersonating you, let's make an if statement to check if their name is equal to your name. If the two are equal, then print out a statement saying: Identity theft is not a victimless crime!
if user_name == "Viserion#0025":
    print("Identity theft is not a victimless crime!")

# 3. Let's see if they have the same age as you. Create an if statement to check if your ages are the same, and see if that works. (Hint: Keep in mind, the value of their age, if it was entered by an input statement, is a string. Remember that you cannot compare different kinds of variables to each other, so make the age you are comparing it to a string, or make their age an integer) If your ages are the same, print a statement such as: Hey buddy!
if user_age == 19:
    print("Hey buddy!")

# Possible Solution:

# name = input("What is your name? ")
# age = input ("What is your age? ")
# print("My name is " + name + " and I am " + age + " years old.")
# # Let's say my name is Lucy
# if name == "Lucy":
#     print("Identity theft is not a victimless crime!")
# if int(age) == 21:
#     print("Hey buddy!")
