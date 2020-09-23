# Here are some exercises to try:

# 1. We have the same list as last time, yet some new additions. Set students equal to [Robert", " Jane", "Adam", "Bailey", "Catherine"], and another list new_students equal to ["Gordon", "Joanne", "Helen"].
students = ["Robert", "Jane", "Adam", "Bailey", "Catherine"]
new_students = ["Gordon", "Joanne", "Helen"]

# 2. Loop through new_students and append each student to list students .
for student in new_students:
    students.append(student)

# 3. There is a new Python 3 class opening on Udemy, however, there are only 5 spots available. Create a new list python_students and set it equal to an empty list.
python_students = []

# 4. Create a while loop with the condition that the length of python_students is less than 5.
while len(python_students) < 5:

    # 5. Inside the while loop, use the .pop() method to take a student off of students and append it to python_students.
    python_student = students.pop()
    python_students.append(python_student)

# 6. Print python_students.
print(python_students)


# Solution:

# students = ["Robert", "Jane", "Adam", "Bailey", "Catherine"]
# new_students = ["Gordon", "Joanne", "Helen"]
# for student in new_students:
#   students.append(student)
# python_students = []
# while len(python_students) < 5:
#   python_student = students.pop()
#   python_students.append(python_student)
# print(python_students)