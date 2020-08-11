Here are some exercises to try:



1. Set a variable equal to the list: ["ApPLeS aND BAnanAs", "romeo/and/juliet"]

2. Print out the first element of the list in all caps.

3. Print out the first element of the list in all lowercase.

4. Set a variable book equal to the second element of the list.

5. Reassign book to book split by the "/" character.

6. Create a variable novel and set it equal to a string with a single space.

7. Reassign that novel to book joined by novel.

8. Print novel in a titlized manner.



Solution:

weird_list = ["ApPLeS aND BAnanAs", "romeo/and/juliet"]
print(weird_list[0].upper())
print(weird_list[0].lower())
book = weird_list[1]
book = book.split("/")
novel = " "
novel = novel.join(book)
print(novel.title())