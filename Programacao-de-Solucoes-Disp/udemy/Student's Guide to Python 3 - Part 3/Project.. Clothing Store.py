# In this project, you will use loops to manage the data for a clothing store.

# 1. Make three lists: products = ["t-shirt", "khakis", "jeans", "hoodie", "coat", "scarf", "socks", "cardigan", "dress"], prices = [14, 23, 25, 27, 40, 15, 5, 30, 36], and inventory = [40, 30, 30, 35, 20, 35, 20, 15, 25]. prices has the price of each corresponding item in products, and inventory shows how many of each corresponding item is in stock.
products = ["t-shirt", "khakis", "jeans", "hoodie", "coat", "scarf", "socks", "cardigan", "dress"]
prices = [14, 23, 25, 27, 40, 15, 5, 30, 36] 
inventory = [40, 30, 30, 35, 20, 35, 20, 15, 25]

# 2. The manager of the store wants to know how many total items the store has. Use a for loop to find the sum of all elements in inventory and print the result.
total_items = 0
for item in inventory:
  total_items+=item

print(total_items)

# 3. The manager also wants to know the total price of all the items in the store. To find this, we will need to create a list of total_price that will hold the values of the total value of each item. For example, because there are 40 t-shirts and each costs $14, the first element of total_price should be 40*14 = 560. Set total_price equal to an empty list for now.

# 3a. Loop through range(len(products)) with a variable num and on each iteration, append the value of prices[num]*inventory[num] to total_price. If you're feeling confident - you can actually do this using list comprehension! Instead of setting total_price equal to an empty list, set it equal to the list comprehension syntax.
total_price = [prices[num]*inventory[num] for num in range(len(products))]

# 3b. Now that we have our completed total_price find the sum of all the elements in the list and print the result.
print(sum(total_price))

# 4. The inventory is actually from last week, it turns out. We need to update it with the shipments from yesterday. 20 more of each item was brought in, so update inventory to reflect that. Try using list comprehension to do this, but if you can't, just use a for loop.
inventory = [item+20 for item in inventory]

# 5. A strange customer just asked if they could keep buying 2 t-shirts until the number of t-shirts in the inventory reached a multiple of 3. Use a while loop to fulfill his request, making sure to store how many t-shirts the customer buys in a separate variable and updating the number of shirts in the inventory every time the customer buys 2. Remember, a number is a multiple of 3 if that number % 3 == 0.
customer_shirts = 0 
while (inventory[0]%3 != 0):
    customer_shirts+=2
    inventory[0]-=2

# 6. Before we calculate how much his total will cost, the store announced a huge sale - 40% off on each item! Update prices to reflect that change.
prices = [price*0.6 for price in prices]

# 7. Now calculate how much the customer's t-shirts will cost and print the result.
print(customer_shirts*prices[0])

# 8. Finally, the store wants to advertise their budget options, so create another list budget that has items from products that are less than $25. Use list comprehension to achieve this.
budget = [products[num] for num in range(len(products)) if prices[num] < 25]
print(prices)
print(budget)