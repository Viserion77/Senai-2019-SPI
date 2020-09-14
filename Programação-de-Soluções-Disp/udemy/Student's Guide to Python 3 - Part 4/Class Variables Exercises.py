# Here are some exercises to try:

# 1. Delete the pass statement in your Circle function.


# 2. Let's add some variables to the class. Because these are class variables, they must pertain to all objects of that class, not just a single object. So, pi is a constant variable in all circles. Define a class variable pi to be 3.14.
class Circle():
    pi = 3.14

    # 3. Another property of circles is that they are round. Define a class variable roundness and set it equal to True.
    roundness = True


    # 4. Finally, define a class variable dimension equal to "2D".
    dimension = "2D"


# 5. Make an instance of the class called circle1 and print all of the class variables of circle1.
circle1 = Circle()

# 6. If all of your code is correct, you can delete the print statements.
print(circle1.pi)
print(circle1.roundness)
print(circle1.dimension)

# Solution:

# class Circle():
#   pi = 3.14
#   roundness = True
#   dimension = "2D"
#  
# circle1 = Circle()
# print(circle1.pi)
# print(circle1.roundness)
# print(circle1.dimension)