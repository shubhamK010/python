#################################################
#  01.09.2022 
#################################################
# TOPICS TO BE COVERED  
# 👉 FLOW CONTROL IN PYTHON AND OPERATORS
#################################################

# COMPARISON


'''
Python supports the usual comparison conditions from mathematics:
Equals:                     a == b # single ' = ' means assignmnet operator 

Not Equals:                 a != b
Less than:                  a < b
Less than or equal to:      a <= b
Greater than:               a > b
Greater than or equal to:   a >= b
'''

# Logical operators
#  AND , OR ,NOT 
# Identity operators
#  IS , NOT IS 
# Membership operators
# IN , NOT IN 



# marks = int(input("Enter your marks :"))

# print(type(marks))

# if marks >= 35:
#     print("You have passed !!! Congrats")
# else:
#     print("You have Failed !!! Sorry")


#################################################
# Membership operators
# IN , NOT IN 
#################################################


roll_num = int(input("Enter your roll num :"))
age_candidate = int(input("Enter your age  :"))

print(type(roll_num))
list1_pass = [2,4,6,8,10] 

if roll_num in list1_pass and age_candidate > 18:

    print("your num is present in the given list1 , you have passed ")
else:
    print("your num is not  present in the given list1 , sorry ")






#################################################
# TRUTHY VALUES
# https://docs.python.org/3/library/stdtypes.html#truth-value-testing
#################################################

# Falsy Values Includes:
# 1) Sequences and Collections:
# Empty lists []
# Empty tuples ()
# Empty dictionaries {}
# Empty sets set()
# Empty strings ” “
# Empty ranges range(0)
# 2) Numbers: Zero of any numeric type.
# Integer: 0
# Float: 0.0
# Complex: 0j
# 3) Constants:
# None
# False






if 1 : #this is always true
    print("I am running")
else:
    print("I am  inside else")


if 0 : #this is always false
    print("I am admin")
else:
    print("I am  HR dept")


# finding boolean values 

print(bool(0))
print(bool(1))
print(bool([]))
print(bool({}))



if [] : #this is always false since its an empty list
    print("I am admin")
else:
    print("I am  HR dept")