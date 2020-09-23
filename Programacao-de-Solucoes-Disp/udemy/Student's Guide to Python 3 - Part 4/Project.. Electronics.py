# In this project, you will be creating classes to manage the inventory of an electronics store.
# 
# 
# 
# 1. First, because this is an electronics store, we will need to create the class Electronic. This class should have a class variable uses_electricity set to True and on set to False. This class, when initialized, should take in parameters price, model, plug_in, and battery, where model will be set to the year that the electronic device was made, plug_in and battery will be boolean variables referring to whether the electronic uses a battery or needs to be plugged into an outlet. (Don't forget to set self.price = price for all parameters)
# 
# 2. When printing an object of class Electronic (hint: __repr__), Python should print a statement such as the following: "Model: 2017, needs to be plugged in".
# 
# 3. Create two class methods: toggle_on and toggle_off that when called on, turn the class variable on to either True or False (Hint: you need to use self.on)
# 
# 4. Create a class Vacuum that inherits from the class Electronic. It should have a class variable places_cleaned set to an empty list.
# 
# 5. In addition to the methods that are already defined, define one more method clean that takes in a parameter place. Append place to your places_cleaned variable, however, if on is False, it should not append anything and instead print the statement "Your device is turned off". (Hint: to end a function early, just return nothing and the function will end)
# 
# 6. Let's create an object in the Vacuum class called home_vacuum that takes in parameters 500, 2017, False, True. Print home_vacuum.
# 
# 7. Turn the vacuum on and have it clean "Living Room", "Master Bedroom", "Kitchen", "Guest Bedroom". Then print places_cleaned for home_vaccum
# 
# 8. Create another class Phone that inherits from Electronic. It should have browsing_history set to an empty list and last_called set to an empty string.
# 
# 9. Redefine the __init__ function with the same parameters and also adding a typephone parameter and use super() so that you don't have to redefine the variables. After calling super() simply define typephone. That will hold information as to whether our phone is an Apple phone or an android phone.
# 
# 10. Define a new function call that takes in a parameter name. Only execute the function if on is True, otherwise print the same statement as before and end the function. Call should print a statement "Calling {name}" and set last_called to name.
# 
# 11. Define a second function browse that takes in a parameter url. Again, if on is False, print the same statement as before and end the function. Otherwise, add url to browsing_history.
# 
# 12. Create an object personal_phone in the Phone class that takes in 1000, 2019, False, True, "iPhone". Turn the phone on and call "Jane".
# 
# 13. Browse the Udemy website, Google, and YouTube. Print the object's last_called and browsing_history.
# 
# 14. Finally, let's go back to the Electronic class and add a function to repurpose the + feature for our Electronics. (Hint: to repurpose +, we need to use a dunder method __add__). Adding two electronics together should return their combined price.
# 
# 15. Print the result of home_vacuum + personal_phone.
# 
# 16. Congratulations! You made multiple classes with inheritance to manage the different electronics of an electronics store!

class Electronic():
  uses_electricity = True
  on = False

  def __init__(self, price, model, plug_in, battery):
    self.price = price
    self.model = model
    self.plug_in = plug_in
    self.battery = battery

  def __repr__(self):
    if self.plug_in == True:
      fill = "needs to be plugged in."
    else:
      fill = "needs a battery"
    return f"Model: {self.model}, {fill}"

  def toggle_on(self):
    self.on = True

  def toggle_off(self):
    self.on = False

  def __add__(self, Electronic):
    return self.price + Electronic.price

class Vacuum(Electronic):
  places_cleaned = []

  def clean(self, place):
    if self.on == False:
      print("Your device is turned off")
      return
    else:
      self.places_cleaned.append(place)

class Phone(Electronic):
  last_called = ""
  browsing_history = []

  def __init__(self, price, model, plug_in, battery, typephone):
    super().__init__(price, model, plug_in, battery)
    self.typephone = typephone

  def call(self, name):
    if self.on == False:
      print("Your device is turned off")
      return
    else:
      self.last_called = name
      print(f"Calling {name}")
    
  def browse(self, url):
    if self.on == False:
      print("Your device is turned off")
      return
    else:
      self.browsing_history.append(url)

home_vacuum = Vacuum(500, 2017, False, True)
home_vacuum.toggle_on()
home_vacuum.clean("Living Room")
home_vacuum.clean("Master Bedroom")
home_vacuum.clean("Kitchen")
home_vacuum.clean("Guest Bedroom")
print(home_vacuum.places_cleaned)

personal_phone = Phone(1000, 2019, False, True, "iPhone")
personal_phone.toggle_on()
personal_phone.call("Jane")
personal_phone.browse("Udemy")
personal_phone.browse("Google")
personal_phone.browse("Youtube")
print(personal_phone.browsing_history, personal_phone.last_called)

print(personal_phone + home_vacuum)