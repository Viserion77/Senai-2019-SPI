# Here are some exercises to try:

# 1. Given a dictionary classroom = {"Ms. Valdes":["John", "Gloria", "Sam"], "Mr. Duncan":["Ashley", "Jenna", "Rick"], "Ms. Anderson":["Will", "Sonia", "Andy"]}, iterate through and print only the teachers' names.
classroom = {"Ms. Valdes":["John", "Gloria", "Sam"], "Mr. Duncan":["Ashley", "Jenna", "Rick"], "Ms. Anderson":["Will", "Sonia", "Andy"]}

# 2. Print a list of all values of the dictionary.
for teacher in classroom.keys():
    print(teacher)

# 3. Using nested loops, print each student's name individually.
for students in classroom.values():
    for student in students:
        print(student)

# 4. Finally, let's print each key and value of this dictionary.
for teacher, students in classroom.items():
    print(teacher, students)

# Solution:

# classroom = {"Ms. Valdes":["John", "Gloria", "Sam"], "Mr. Duncan":["Ashley", "Jenna", "Rick"], "Ms. Anderson":["Will", "Sonia", "Andy"]}
#  
# for teacher in classroom.keys():
#   print(teacher)
#  
# print(classroom.values())
#  
# for students in classroom.values():
#   for student in students:
#     print(student)
#  
# for teacher, students in classroom.items():
#   print(teacher, class)