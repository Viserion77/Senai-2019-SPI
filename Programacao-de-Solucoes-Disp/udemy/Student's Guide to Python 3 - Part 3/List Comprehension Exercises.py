# Here are some exercises to try:

# 1. We have a list of usernames ["lemonlime35", "slo99", "hydrohomie", "ayejay", "breadium", "art_allie09", "nevertheless49"].
usernames = ["lemonlime95", "slo99", "hydrohomie", "ayejay", "breadium", "art_allie09", "nevertheless49"]

# 2. Using list comprehension, create a list from usernames of only valid_usernames. A username that has the number 9 as its last character is considered valid. Use type(username[-1]) is int to check this. Print valid_usernames
valid_usernames = [username for username in usernames if username[-1] == "9"]
print(valid_usernames)

# 3. We need to make these usernames official! From valid_usernames, using list comprehension, create the same list where each element has an "@" symbol in front. Print official_usernames.
official_usernames = ["@" + username for username in valid_usernames]
print(official_usernames)

# Solution:

# usernames = ["lemonlime95", "slo99", "hydrohomie", "ayejay", "breadium", "art_allie09", "nevertheless49"]
# valid_usernames = [username for username in usernames if username[-1] == "9"]
# print(valid_usernames)
# official_usernames = ["@" + username for username in valid_usernames]
# print(official_usernames)