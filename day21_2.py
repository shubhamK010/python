#"def" = definition means defining the function
# Syntax of User defined function:
from re import A


def multiply():   # rules for naming a function is same as that of a variable
    a = 5*6
    return a # this will return the value of "a" when function is called

answer = multiply()
print(answer)


#using parameters in User defined function

def multiply(x,y):
    a =x*y
    return A

answer = multiply(5,6) # position of argument is important
print(answer)


def multiply(x=0,y=0):
    a =x-y
    return a
answer = multiply(5,6) #the given argument will overwrite the initial values....mhanje apan parameters madhe value nahi lihu shakat
print(answer)