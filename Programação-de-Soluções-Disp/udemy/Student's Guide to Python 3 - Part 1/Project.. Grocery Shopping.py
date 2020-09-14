# In this project, you will create a system to manage grocery items and shopping lists and prices.
# ok


# Instructions:
# humm

# 1. Let's fill up our grocery store! Define 3 variables named item1, item2, and item3 and make them equal to the strings tomato, ham, and lettuce.
item1, item2, item3 = "tomato", "ham", "lettuce"

# 2. How many of each item are there? Set variables named item1_count, item2_count, and item3_count equal to the number of each item you want there to be.
item1_count, item2_count, item3_count = 0, 1, 2

# 3. Let's set the price of these items. Set variables named item1_price, item2_price, and item3_price equal to an appropriate price.
item1_price, item2_price, item3_price = 3, 4, 5,

# 4. What do we have in our grocery store so far? Print a statement such as: Our grocery store has tomato, ham, and lettuce using string concatenation.
print("Our grocery store has "+item1+", "+item2+", and "+item3)

# 5. A customer is asking for the price of ham. Print out a statement such as: The price of ham is item2_price, using the variable item2_price and using string concatenation. Remember that integers or floats cannot be concatenated with strings so use str() to turn them into strings.
products = [[item1, item1_count, item1_price],
            [item2, item2_count, item2_price],
            [item3, item3_count, item3_price]]
print("products prices")
for product in products:
    print("O preço do "+product[0]+" é " + str(product[2]))

# 6. We have to have a sales tax, so define a variable sales_tax and set it equal to 0.0725.
sales_tax = 0.0725

# 7. The customer that was just asking for the price of ham wants to buy some things. Let's create a variable called customer_total so that we know how much their total will be, and let's create an empty string by setting customer_items = "" so that we can add what they are buying.
customer_total = 0
customer_items = ""

# 8. Fill up their cart! Add items to customer_items using string concatenation, and make sure to update the customer_total with the prices of the items. Also make sure to subtract the count of the items once a customer buys that item.
customer_items = []
for product in products:
    if (product[1] >= 1):
        product[1] = product[1] - 1
        customer_total = customer_total + product[2]
        customer_items.append([product[0], 1, product[2]])

# 9. Are they done? If so, let's set customer_total = customer_total + customer_total*sales_tax in order to account for tax.
customer_total = customer_total + customer_total*sales_tax

# 10. Let's print this customer a receipt! Print a statement showing the customer what they bought, and how much their total came out to be. Their total might come out as a number that cannot be paid in dollars and cents, so let's round that using the round(customer_total, 2) function. The 2 lets the computer know that we want customer_total to be rounded to 2 decimal places. Let's also print out how many of each item are left at our grocery store.
customer_total = round(customer_total, 2)
print("this customer a receipt!")
for customer_item in customer_items:
    print(str(customer_item[1]) + " - " + customer_item[0] + " | U$" + str(customer_item[2]))
print("how many of each item are left at our grocery store?")
for product in products:
    print(product[0] + ": " + str(product[1]))

# 11. Congratulations! You created a catalog for our grocery store and left a customer feeling very satisfied!
# :D