
#Wrtite a code to check if a number is a palindrome by taking input from user

def is_palindrome(string):
    backwards = string[::-1]
    print(backwards)
    return backwards.casefold()==string.casefold()

word = input("Please Enter the Number:")

if is_palindrome(word):
    print("Given Number is a Palindrome")
else:
    print("Given Number is not a Palindrome")    