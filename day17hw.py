
# counting number of spaces in a given string/senetence


num1 = "Min Skole 12 3"
space= 0 #initializing the space value as ZERO

# for i in num1:
#     if(i==' '):
#         space +=1
# print(space)        

#####################or######################

num1 = "Min Sk ole 12 3"
space = 0
for char in num1:
    if char.isspace():
        space +=1
print(space)        


