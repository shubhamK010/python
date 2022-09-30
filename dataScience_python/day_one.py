#################################################
#  31.08.2022 
#################################################
# TOPICS TO BE COVERED  
# 👉 STRINGS
#################################################

# anything that is inside  '' ," ", ''' '''  is considered string in Python*

string1  = 'Hello World'

print(type(string1))
#################################################
# indexing 
#################################################
# print(string1[0])
# print(string1[1])
# print(string1[2])
# print(string1[3])
# print(string1[10])


#################################################
# SLICING WITH POSITIVE INDEXING
#################################################

string1  = 'Hello World'

# syntax 
# var_name[start : end] # END is always n-1

print(string1[0:4])
print(string1[0:5])
print(string1[6:11])

 
string2 = 'I Love Python3.0'
print(string2[2:7])


#################################################
# SLICING with NEGATIVE INDEXING
#################################################
string3 = 'I Love Python3.0 I Love Python3.0 I Love Python3.0 I Love Python3.01'
string1  = 'Hello World'

print(string1[-5:-1])
print(string1[-5:0])
print(string1[-5:])


print("************")
print(string1[0:])
print(string1[:11])
# var_name[start : end] # END is always n-1
print("************")
print(string1[:])
print(string1[:-1])