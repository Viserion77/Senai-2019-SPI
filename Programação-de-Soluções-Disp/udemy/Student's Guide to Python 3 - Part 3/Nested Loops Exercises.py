# Here are some exercises to try:

# 1. We will use the same list of students from last time: ["robert", "jane", "adam", "bailey", "catherine"].
students = ["robert", "jane", "adam", "bailey", "catherine"]

# 2. Let's begin by creating a for loop, looping through each student.
for student in students:

    # 3. Create a local variable letters and set it equal to an empty list.
    letters = []

    # 4. Nest another for loop, this time looping through each letter of the student's name.
    for letter in student:

        # 5. Append each letter to letters.
        letters.append(letter)

        # 6. After exiting the innermost loop, print letters.
    print(letters)

# Solution:

# students = ["robert", "jane", "adam", "bailey", "catherine"]
# for student in students:
#   letters = []
#   for letter in student:
#     letters.append(letter)
#   print(letters)