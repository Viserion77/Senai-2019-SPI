# Here are some exercises to try:

# 1. Redefine the + function so that it can be used with circles. It should return the sum of the two circles (or semicircles) being added together)
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
 
    def __add__(self, other):
        return self.area()+other.area()
 
class SemiCircle(Circle):
    roundness = False
    fact = "Semicircles are half of circles"
 
    def __init__(self, name, color, radius, closed):
        super().__init__(name, color, radius)
        self.closed = closed
 
    def circumference(self):
        return self.radius*self.pi
 
    def area(self):
        return self.radius**2*self.pi/2

circle1 = Circle("alberto", "rodrigo", 5)
semicircle1 = SemiCircle("robinso", "Valdir", 9, True)

# 2. Test this by adding semicircle1 and circle1 together and printing the result.
print(circle1.area())
print(semicircle1.area())
print(semicircle1 + circle1)

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
#   def __add__(self, other):
#     return self.area()+other.area()
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
# print(circle1.area())
# print(semicircle1.area())
# print(semicircle1 + circle1)