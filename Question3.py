# Write a program that ask the user to input a text and then recognises palindromes
#(i.e. words that look the same written backwards). For example, "radar" is a palindrome.


word = input("Enter a word to test for palindrome: ")
word1 = word.lower()
while word != "":
    if str(word1) == str(word1[::-1]):
        print ("True")
    elif str(word1) != str(word1[::-1]):
        print ("False")
    
    word = input("Enter a word to test for palindrome: ")
