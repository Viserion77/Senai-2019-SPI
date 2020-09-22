# Here are some exercises to try:

# 1. Under your class variables, create an __init__ function. Pass name, color, and radius as parameters, and define them as variables of the object. These are specific to each object of this class. (Don't forget to pass self as a parameter)
class Circle():
    pi = 3.14
    roundness = True
    dimension = "2D"

    # 2. When an instance of the class is called, have it print out a statement in the following format: "A [color] circle [name] with a radius of [radius] has just been created!".
    def __init__(self, name, color, radius):
        self.name = name
        self.color = color
        self.radius = radius
        print(f"A {color} circle {name} with a radius of {radius} has just been created!")

        # 3. When we try to print an object of this class, we want it to display information about that object. So, define a __repr__ function that when called upon by a print statement of Circle, returns the name, color, and radius of the object.
    def __repr__(self):
        return f"Name: {self.name} \nColor: {self.color}\nRadius: {self.radius}"

# 4. Edit circle1 so that it passes through a name, color, and radius.
circle1 = Circle("Fred", "red", 5)

# 5. Print circle1.
print(circle1)


# 6. If your code is correct, you can remove the print statement.


# Solution:

# class Circle():
#   pi = 3.14
#   roundness = True
#   dimension = "2D"
#  
#   def __init__(self, name, color, radius):
#     self.name = name
#     self.color = color
#     self.radius = radius
#     print(f"A {color} circle {name} with a radius of {radius} has just been created!")
#  
#   def __repr__(self):
#     return f"Name: {self.name} \nColor: {self.color}\nRadius: {self.radius}"
#  
#  
# circle1 = Circle("Fred", "red", 5)
# print(circle1)