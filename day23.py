# to check if a word is a palindrome 
def is_palindrome(string):
    backwards = string[::-1] 
    print(backwards)
    return backwards.casefold() == string.casefold()


# Checking if a Sentence is a palindrome
def palindrome_sentence(sentence):
    string = ""
    for char in sentence.casefold():# USING CASEFOLD TO MAKE LOWER CASE 
      if char.isalpha(): #  checking characters in the  sentence using .isalpha()
        string= char +  string # storing only alphabets in the variable "string"
    print(string)
    # backwards = string[ : :-1]
    # return backwards == string
    return is_palindrome(string) # reusing a code i.e calling another function


sentence = input("Please enter the sentence to check :")
if palindrome_sentence(sentence):
    print("{} is a palindrome".format(sentence))
else:
    print("{} is  not a palindrome".format(sentence))


# function doing task instead of returning a value
def separator(a):
    print("*"*a)

# print(separator())
separator(100)