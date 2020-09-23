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

    # 1. Let's make a function diameter that returns the diameter of that circle. (Don't forget to use self.radius to call the radius)
    def diameter(self):
        return 2*self.radius

    # 2. Repeat for circumference and area. (Reminder, the formulas are 2*pi*r and pi*r^2 respectively)
    def circumference(self):
        return 2*self.radius*self.pi
    def area(self):
        return self.radius**2*self.pi

    # 3. Make a change_radius function that has a parameter change and adds change to the current value of the object's radius.
    def change_radius(self, change):
        self.radius+=change

# 4. Test your functions by first calling change_radius on circle1, passing in a value of -2. Then call each function and print the result. Are they correct?
circle1 = Circle("Fred", "red", 5)
circle1.change_radius(-2)
print(circle1.diameter())
print(circle1.circumference())
print(circle1.area())

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
#  
# circle1 = Circle("Fred", "red", 5)
# circle1.change_radius(-2)
# print(circle1.diameter())
# print(circle1.circumference())
# print(circle1.area())