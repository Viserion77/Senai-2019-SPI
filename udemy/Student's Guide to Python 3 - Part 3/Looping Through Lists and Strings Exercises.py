# Here are some exercises to try:

# 1. Here is a list of students: ["robert", "jane", "adam", "bailey", "catherine"]. Loop through the list and print a greeting to each one of them.
students = ["robert", "jane", "adam", "bailey", "catherine"]

# 2. Create a range based loop of for index in range(len(students)). For each students[index], set it equal to the capitalized value of the name. Print students
for student in students:
    print(f"Hello {student}")

# 3. Loop through each student in the list, and if the student's name starts with the letter A, print their name.
for index in range(len(students)):
    students[index] = students[index].title()
print(students)

# 4. Loop through each letter of the first student in the list and print each letter out.
for student in students:
  if student[0] == 'A':
    print(student)
for letter in students[0]:
  print(letter)

# Solution:

# students = ["robert", "jane", "adam", "bailey", "catherine"]
# for student in students:
#   print(f"Hello {student}")
# for index in range(len(students)):
#   students[index] = students[index].title()
# print(students)
# for student in students:
#   if student[0] == 'A':
#     print(student)
# for letter in students[0]:
#   print(letter)