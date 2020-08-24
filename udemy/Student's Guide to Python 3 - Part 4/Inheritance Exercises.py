# Here are some exercises to try:

class Circle():
    pi = 3.14
    roundness = True
    dimension = "2D"
 
    def __init__(self, name, color, radius):
        self.name = name
        self.color = color
        self.radius = radius
        print(f"A {color} circle {name} with a radius of {radius} has just been created!")
 
    def __repr__(self):
        return f"Name: {self.name} \nColor: {self.color}\nRadius: {self.radius}"
 
    def diameter(self):
        return 2*self.radius
    
    def circumference(self):
        return 2*self.radius*self.pi
 
    def area(self):
        return self.radius**2*self.pi
    
    def change_radius(self, change):
        self.radius+=change

    # 1. Make a class SemiCircle that inherits from Circle.
class SemiCircle(Circle):


    # 2. We need to change some things about SemiCircle, however. Overwrite roundness to be False.
    roundness = False


    # 3. Add another class variable fact and set it equal to "Semicircles are half of circles"
    fact = "Semicircles are half of circles"


# 4. Create an instance of your SemiCircle class called semicircle1. (Remember to initialize it with some variables)
circle1 = Circle("Robert", "Cercy", 5)
semicircle1 = SemiCircle("Daenarys", "Jhown", 9)

# 5. Print the fact of semicircle1.
print(semicircle1.fact)

# 6. If your code is correct, you can delete the print statement.


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
#   def diameter(self):
#     return 2*self.radius
#   
#   def circumference(self):
#     return 2*self.radius*self.pi
#  
#   def area(self):
#     return self.radius**2*self.pi
#   
#   def change_radius(self, change):
#     self.radius+=change
#  
# class SemiCircle(Circle):
#   roundness = False
#   fact = "Semicircles are half of circles"
#  
# circle1 = Circle("Fred", "red", 5)
# semicircle1 = SemiCircle("Bob", "blue", 9)
# print(semicircle1.fact)