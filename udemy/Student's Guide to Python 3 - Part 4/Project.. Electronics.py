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