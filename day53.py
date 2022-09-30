#################################################
# Exception handeling in Python
#################################################

#  Errors vs  Exceptions ??


# a = 100
# b = a/0

# print(b)


# a = b
# print(" we are outside the try block")

# syntax

# try:
#   code 
# except:
#   remarks/comment

# try:
#   a = b
# except:
#   print("something went wrong")



# try:
#   a = b
# except Exception as e:
#   print(e)

# print(" we are outside the try block")



# how to get info about  Exception in python 

# print(dir(Exception))
# help(Exception)

# HW exit code = 0 
# code execution status was ??


# try:
#   a = b
# except Exception as e:
#   print(e)



try:
  a = int(input("ENter 1st num:"))
  b = int(input("ENter 2nd num:"))
  d = int(input("ENter the index position :"))
  c = a/b
  print(c)
  list1 = [1,2,3,4,5]
  print(list1[d])

except NameError:
  print(" Enter non zero number , division by zero not defined") 
# except NameError:
#   print(" You have not enterd the value of c. Please enter value of c")
except IndexError:
  print(" Enter index value  less than 5")
except Exception as e: # this should be at the end of try except block
  print(e)

else:
  print("the code is excuted successfully")

finally:
  print(" This will always be executed")