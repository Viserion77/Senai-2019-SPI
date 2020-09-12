# Here are some exercises to try:

class Circle():
    pi = 3.14
    roundness = True
    dimension = "2D"
 
    def __init__(self, name, color, radius):
        self.name = name
        self.color = color
        self.radius = radius
 
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
 
class SemiCircle(Circle):
    roundness = False
    fact = "Semicircles are half of circles"

    # 1. First, let's delete the print statement from our __init__ function in the Circle class, as it is a bit repetitive to have that and the __repr__ which basically both print out the same thing.
    def __init__(self, name, color, radius, closed):

        # 2. Let's overwrite the __init__ statement in our SemiCircle class and pass the same parameters in as before, and add one more: closed - a boolean variable referring to if the semicircle has a line connecting the two end of the half circle, or if it is quite literally half of a circle. Set up those variables, using the super() function and then setting up closed manually.
        super().__init__(name, color, radius)
        self.closed = closed


# 3. Let's overwrite the circumference and area functions to reflect a semicircle instead of a circle.
    def circumference(self):
        return self.radius*self.pi
    def area(self):
        return self.radius**2*self.pi/2

# 4. Try printing the circumference and area of semicircle1 to see if they are correct. Make sure to pass in a value for closed for semicircle1.
circle1 = Circle("alberto", "rodrigo", 5)
semicircle1 = SemiCircle("robinso", "Valdir", 9, True)
print(semicircle1.area())
print(semicircle1.circumference())

# 5. If your code is correct, you can delete the print statements.


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
#   def __init__(self, name, color, radius, closed):
#     super().__init__(name, color, radius)
#     self.closed = closed
#  
#   def circumference(self):
#     return self.radius*self.pi
#  
#   def area(self):
#     return self.radius**2*self.pi/2
#  
# circle1 = Circle("Fred", "red", 5)
# semicircle1 = SemiCircle("Bob", "blue", 9, True)
# print(semicircle1.area())
# print(semicircle1.circumference())