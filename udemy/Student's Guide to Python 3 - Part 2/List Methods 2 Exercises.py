# Here are some exercises to try:

# 1. Create a list of 6 subjects in school.
list = ['study 1','study 2','study 3','study 4','study bastante','study 7']

# 2. Print your least favorite subject in school, and then remove it from the list.
print(list[4])
list.remove('study bastante')

# 3. Make a variable four and set it equal to the fourth element of the list which you removed from the list.
four = list.pop(3)

# 4. Print out four, and then print out index four of the list to make sure you removed the element.
print(four+list[3])

# Solution:

# subjects = ["English", "Calculus", "Physics", "US History", "Psychology", "Biology"]
# print("English") #or print(subjects[0])
# subjects.remove("English")
# four = subjects.pop(3) #remember that lists begin at index 0
# print(four)
# print(subjects[3])