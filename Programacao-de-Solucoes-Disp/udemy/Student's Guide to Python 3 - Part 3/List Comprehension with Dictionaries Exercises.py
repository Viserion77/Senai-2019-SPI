# Here are some exercises to try:

# 1. Given a list of books and a list of authors: ["Lord of the Rings", "Old Man and the Sea", "Oliver Twist", "To Kill a Mockingbird"], ["J.R.R. Tolkien", "Ernest Hemingway", "Charles Dickens", "Harper Lee"], create a dictionary using list comprehension. Print the dictionary.
books = ["Lord of the Rings", "Old Man and the Sea", "Oliver Twist", "To Kill a Mockingbird"]
authors = ["J.R.R. Tolkien", "Ernest Hemingway", "Charles Dickens", "Harper Lee"]
catalogue = {book:author for book,author in zip(books, authors)}
print(catalogue)

# 2. We want to give some more clarification that each key is a book and each value is an author. Make another dictionary from the two lists, but this time with each key being preceded with "Book:" and each value being preceded with "Author:". So the first item of the dictionary should be {"Book: Lord of the Rings":"Author: J.R.R. Tolkien"}. Print this as well.
specific_catalogue = {"Book: "+book:"Author: "+author for book,author in zip(books, authors)}
print(specific_catalogue)

# Solution:

# books = ["Lord of the Rings", "Old Man and the Sea", "Oliver Twist", "To Kill a Mockingbird"]
# authors = ["J.R.R. Tolkien", "Ernest Hemingway", "Charles Dickens", "Harper Lee"]
# catalogue = {book:author for book,author in zip(books, authors)}
# print(catalogue)
# specific_catalogue = {"Book: "+book:"Author: "+author for book,author in zip(books, authors)}
# print(specific_catalogue)