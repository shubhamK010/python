# TODAYS CODE 
# =======================================

# we have all the code inside the .py file
# but we want more functionalities to be used in the code
# we import module
# modules are collection of Function 
# we have 3rd party modules as well as in built ones
# inbuilt are imported automatically without calling 
# eg: print()
# how to import a module 
# 1. importing complete module as it is
import turtle
# how to see what is coming with this module
# use dir() this is not the dir used in windows
print(dir(turtle))
print(type(dir(turtle)))
# more readable form as this is a list
for i in dir(turtle):
    print(i)
# for more help related to functions/methods coming with module
help(turtle.circle)

# 2. to import only specific functions
# this is good if we are using limited fun from the module as calling is easy
# but variables have to be choosen properly to avoid conflict

from turtle import circle , forward , done
turtle.forward(100)
forward(100)
done()
# use either of the method 1 or 2 not both for importing any module
# else code will misbehave 
# 
# 
# 3.  3rd method but not recommended
from turtle import *
turtle.forward(100)
forward(100)
done()