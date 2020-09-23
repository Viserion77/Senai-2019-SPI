# Here are some exercises to try:

# 1. Create a dictionary bottles with the following pairs: Coke-21, Sprite-44, Water-35, Iced Tea-50, Lemonade-44.
bottles = {"Coke":21, "Sprite":44, "Water":35, "Iced Tea":50, "Lemonade":44}

# 2. Given the following pairs: Fruit Punch-36, Orange Juice-40, Green Tea-33; add them to bottles using only one command.
bottles.update({"Fruit Punch":36, "Orange Juice":40, "Green Tea":33})

# 3. Print how many bottles there are of the following: Orange Juice, Water, and Root Beer. Remember to avoid printing any errors!
print(bottles.get("Orange Juice"))
print(bottles.get("Water"))
print(bottles.get("Root Beer"))

# 4. Remove lemonade from bottles because someone bought all of them! Print out how many bottles there were.
print(bottles.pop("Lemonade", 0))

# 5. Remove root beer from the dictionary as well, and print how many were originally in bottles.
print(bottles.pop("Root Beer", 0))

# 6. Print bottles.
print(bottles)

# Solution:

# bottles = {"Coke":21, "Sprite":44, "Water":35, "Iced Tea":50, "Lemonade":44}
# bottles.update({"Fruit Punch":36, "Orange Juice":40, "Green Tea":33})
# print(bottles.get("Orange Juice"))
# print(bottles.get("Water"))
# print(bottles.get("Root Beer"))
# print(bottles.pop("Lemonade", 0))
# print(bottles.pop("Root Beer", 0))
# print(bottles)