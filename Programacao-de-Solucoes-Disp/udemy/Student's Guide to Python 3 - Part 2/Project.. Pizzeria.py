# In this project, you will manage the data and information for a pizzeria.

# 1. Make a list of pizzas: Pepperoni, Combination, Cheese, Margherita, Hawaiian, Sausage.
pizzas=["Pepperoni", "Combination", "Cheese", "Margherita", "Hawaiian", "Sausage"]

# 2. Make a list of prices of those pizzas: 5, 8, 4, 5, 6, 7.
prices=[5, 8, 4, 5, 6, 7]

# 3. Make a variable pizzaprices that uses zip() to tie these two lists together. zip() will take two lists and put their values in what are known as tuples - basically coordinates. For example, the first item in our new list would be (5, Pepperoni) if we zipped the prices, then the pizzas like this: pizzaprices = zip(prices, pizzas). However, zip() does not combine two lists into a third list, so in order to make it an actual list, we will need to use the list() function. So, our code would look something like this: pizzaprices = list(zip(prices, pizzas)).
pizzaprices=list(zip(pizzas,prices))

# 4. Uh oh! It looks like our prices are jumbled up on the menu. We need them to be in order, so sort pizzaprices to make it right again.
pizzaprices.sort()

# 5. A customer walks in and asks for the most expensive pizza. Print the last item in our list.
print(pizzaprices[-1])

# 6. Three boys walk in and request for the three cheapest pizzas. Print out the first three items of the list.
print(pizzaprices[:3])

# 7. These three women only want every other pizza starting from the cheapest pizza. Print those items out.
print(pizzaprices[::2])

# 8. With all this ordering, we've run out of cheese pizza. Remove the first item of our list.
pizzaprices.pop(0)

# 9. Finally, print out all the remaining pizzas on our list!
print(pizzaprices)