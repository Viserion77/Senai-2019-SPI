In this project, you will manage the data for the books in a library.



1. There is a list of books at the library, but it looks like the dataset has been corrupted! Set a variable catalogue equal to the string: "Pride9and9Prejudice;;To9Kill9a9Mockingbird;;tHe9GrEAt9gATsBy;;One9Hundred9Years9of9Solitude;;In9Cold9Blood;;Wide9Sargasso9Sea;;Brave9New9World;;I9Capture9the9Castle;;Jane9Eyre;;Crime9and9Punishment;;The9Secret9History;;The9Call9Of9The9Wild"

2. We need to decode it! Let's begin with replacing all the instances of 9 with a space, as each word needs to be separated by a space. Reassign catalogue to that value.

3. Let's reassign catalogue to the split value of catalogue. We will want to split the string by ";;" because that is what separates each book from each other.

4. Now catalogue is equal to a list of different books! Print the value of catalogue. Is there any title that seems off to you? Let's fix The Great Gatsby. Set the third element of the list equal to the titlized value of the third element of the list. (Use .title() )

5. Print a statement saying "The Great Gatsby was fixed" using fstrings and by accessing lists.

6. It turns out, there was one more book in the library's archives that wasn't registered. Set a list equal to ["The", "Invisible", "Man"].

7. We need to piece this together! Set a variable last_book equal to the prior list joined by " ".

8. Add last_book to the catalogue.

9. Finally, just for fun, let's print out every other letter of the book we just added to the catalogue to make sure it was added correctly.

