Here are some exercises to try:



1. Set a variable equal to the sentence: "I like birds."

2. Try printing the period in the sentence.

3. Try printing the letter 'l' in the sentence.

4. Print each word using slicing strings.

5. Print the sentence without the period.

6. Someone has encrypted a message in the string "Ifdlasoasvqwesupjhysdtvfhsmoasn". The key is to get every third letter. Print the decoded message.



Solution:

sentence = "I like birds."
print(sentence[-1])
print(sentence[0])
print(sentence[0], sentence[2:6], sentence[7:12])
print(sentence[:12])
code = "Ifdlasoasvqwesupjhysdtvfhsmoasn"
print(code[::3])