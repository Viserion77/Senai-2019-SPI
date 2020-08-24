# Here are some exercises to try:

# 1. We have a list of names that start with A: ["Ashly", "Alex", "Ava", "Adam", "Agatha", "Amy", "Ben", "Arthur", "Arnold", "Amelia", "Aidan"].
names = ["Ashly", "Alex", "Ava", "Adam", "Agatha", "Amy", "Ben", "Arthur", "Arnold", "Amelia", "Aidan"]

# 2. It looks like there is one name that starts with a different letter! Loop through the list and if the first letter of the name does not begin with an A, print the name and break from the for loop.
for name in names:
    if name[0] != "A":
        print(name)
        break

# 3. On the converse, we can find the name that is different another way. Loop through each name, and if the name starts with the letter A, simply continue. Otherwise, print the name.
for name in names:
    if name[0] == "A":
        continue
    else:
        print(name)

# Solution:

# names = ["Ashly", "Alex", "Ava", "Adam", "Agatha", "Amy", "Ben", "Arthur", "Arnold", "Amelia", "Aidan"]
# for name in names:
#   if name[0] != "A":
#     print(name)
#     break
# for name in names:
#   if name[0] == "A":
#     continue
#   else:
#     print(name)