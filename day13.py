# printing table of 8 upto 4
print(8*1)
print(8*2)
print(8*3)
print(8*4)
print(" The table of 8*1 is 8" )

# printing table of 5 upto 9
print(5*1)
print(5*2)
print(5*3)
print(5*4)
print(5*5)
print(5*6)
print(5*7)
print(5*8)
print(5*9)
print(" The table of 5*1 is 5" )

# using FOR for simplifying the code !!!


print("****using for ********")



for i in range(1,11): #for should end with ":"
    print(" The table of 8 *" ,i ," is :" ,8*i) # be careful to use proper indentation
    print("*********")




# List first 10 numbers

for i in range(1,11):
    print(i)
    print("*********")

# using IF flow control for conditional output 

# checking if the citizen is eligible to vote : age 18+
name_citizen = input("Enter your name : ")
age_citizen = int(input("Enter you age :")) 
if age_citizen >= 18 :
    print("You are eligible Mr." , name_citizen)
    print("You your voting right carefully ")
else: 
    print("Your age is less than 18 Mr. " , name_citizen)
    print("You are not not eligible to vote ")