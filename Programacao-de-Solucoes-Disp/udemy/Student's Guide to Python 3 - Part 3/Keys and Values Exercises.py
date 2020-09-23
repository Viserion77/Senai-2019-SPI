# Here are some exercises to try:

# 1. Create a dictionary inventory with the following key/value pairs: sneakers:28, sandals:34, slippers:25, boots:19, high heels:23, flip flops:12, Crocs:45.
inventory = {"sneakers":28, "sandals":34, "slippers":25, "boots":19, "high heels":23, "flip flops":12, "Crocs":45}

# 2.  Add a key "cleats" with a value of 11.
inventory["cleats"] = 11

# 3. We need to update the number of sneakers as a shipment of 14 just arrived. Change the value of to match the change.
inventory["sneakers"]+=14

# 4. Let's print out the number of sneakers in the inventory.
print(inventory["sneakers"])

# 5. It turns out that there were actually 35 Crocs, not 45. Let's overwrite the current value of Crocs and replace it with 35.
inventory["Crocs"] = 35

# 6. Print out the number of Crocs in inventory.
print(inventory["Crocs"])

# Solution:

# inventory = {"sneakers":28, "sandals":34, "slippers":25, "boots":19, "high heels":23, "flip flops":12, "Crocs":45}
# inventory["cleats"] = 11
# inventory["sneakers"]+=14
# print(inventory["sneakers"])
# inventory["Crocs"] = 35
# print(inventory["Crocs"])