# In this project, you will manage the data of the grades of students in a classroom.

# 1. You will be working with this dataset: classroom = {"Jay":[69, 67, 74, 90, 94], "Bethany":[68, 76, 82, 81, 86], "Isaac":[98, 64, 94, 95, 89], "Jack":[71, 97, 84, 85, 81], "Aidan":[99, 81, 83, 82, 78]}. This is a dictionary with the students' names as the keys and their scores on the 5 tests this year.
classroom = {
    "Jay": [69, 67, 74, 90, 94],
    "Bethany": [68, 76, 82, 81, 86],
    "Isaac": [98, 64, 94, 95, 89],
    "Jack": [71, 97, 84, 85, 81],
    "Aidan": [99, 81, 83, 82, 78]
}

# 2. Oops! It looks like we forgot to add a student to this dictionary. Add "Bradley":[99, 78, 79, 78, 73]} to the dictionary.
classroom["Bradley"] = [99, 78, 79, 78, 73]

# 3. The teacher needs to modify this dictionary a little bit. She wants "Student: " in front of each student's name. Use list comprehension to create a dictionary updated_classroom that has "Student: " in front of each student's name. (Hint: Instead of zipping 2 lists together, try using classroom.items() instead.)

# 4. Next, the teacher wants a list of all students. Use list comprehension to create a list (not a dictionary) of all the student's names. (Hint: You might want to use updated_classroom.keys()) Print this list.print([name for name in updated_classroom.keys()])
updated_classroom = {
    "Student: " + name: grade
    for name, grade in classroom.items()
}

# 5. It turns out the teacher made a mistake when entering in Bethany's grades. Change her grades to the list [62, 68, 98, 81, 71] instead.
updated_classroom["Student: Bethany"] = [62, 68, 98, 81, 71]
print(updated_classroom)

# 6. We want to print the grades for the students who are asking. Print the grades for Aidan, Julie, and Isaac. Remember to print them safely, as to not throw any errors.
print(updated_classroom.get("Student: Aidan", "No Grades Found"))
print(updated_classroom.get("Student: Julie", "No Grades Found"))
print(updated_classroom.get("Student: Isaac", "No Grades Found"))


# 7. Jay is being transferred to another class. We need to print out his grades so they are recorded by the other class' teacher, and then remove him from our dictionary. Can you do this with just 1 line of code?
print(updated_classroom.pop("Student: Jay", "No Student Found"))


# 8. Finally, we need to print their cumulative grade by taking the average. To add up all the elements in a list, use sum(enter_list_here), and remember to divide it by the number of elements in the list. Do this using list comprehension and create another dictionary final_grades that has the student names and average grade as the key and value.
final_grades = {student:sum(grade)/len(grade) for student,grade in updated_classroom.items()} #grade is a list
print(final_grades)

# 9. Congratulations on finishing dictionaries! Onwards to the final unit of Python!

