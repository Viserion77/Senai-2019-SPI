Here are some exercises to try:



1. Make a list of 5 countries, and print how many elements there are in the list.

2. Add another country to the list.

3. Make a function to print how many elements there are in the list, and call it after you add the country to the list.

4. Replace the print statement from earlier with the function call, and run your program to make sure it is correct.

5. Add the third element of the list to the list again.

6. Print the number of times that element appears in the list.

7. Finally, print the sorted list of countries.

Solution:

countries = ["USA", "China", "France", "Spain", "Egypt"]
print(len(countries)) #replace with elementcount()
countries.append("South Korea")
def elementcount():
    print(len(countries))
elementcount()
countries.append(countries[2]) #remember that lists begin counting at index 0
print(countries.count(countries[2]))
countries.sort()
print(countries)