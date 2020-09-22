# Here are some exercises to try:

# 1. Print every number from 1-20 using a range based loop.
for num in range(1, 21):
    print(num)

# 2. Print every even number from 1-20. (Hint: If the number is divided by 2 and leaves no remainder, it is even.)
for num in range(1, 21):
    if num%2==0:
        print(num)

# 3. Print "Hello!" 10 times.
for num in range(10):
    print("Hello!")

# 4. Create a variable sum that is equal to 0.
sum = 0

# 5. From 1-10, add the number to sum, then after the for loop, print sum.
for num in range(1, 11):
    sum += num
    print(sum)

# Solution:

# for num in range(1, 21):
#   print(num)
# for num in range(1, 21):
#   if num%2==0:
#     print(num)
# for num in range(10):
#   print("Hello!")
# sum = 0
# for num in range(1, 11):
#   sum += num
# print(sum)