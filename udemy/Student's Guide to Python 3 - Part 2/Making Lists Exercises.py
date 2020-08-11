Here are some exercises to try:



1. Make a list of 5 foods.

2. Make a function that returns the first food in the list.

3. Call the function and print the result.

4. What food is at index 4? Think about it and then print the item at index 4 of the list.

5. Print the last element of the list. (Hint: You don't have to know what the size of the list is)



Solution:

foods = ["strawberry", "tomato", "turnip", "burger", "jelly"]
 
def firstfood():
     return foods[0]
 
print(firstfood())
#jelly is at index 4
print(foods[4])
#remember that lists begin at index 0!
print(foods[-1])