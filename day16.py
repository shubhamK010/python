

#  HELPING A TRAVELLER
sleepy = input("Are you sleepy y/n:")
thirsty = input("Are you thirsty y/n:")
travelling  = input("Are you travelling y/n:")
less_money  = input("Are you having  less_money y/n :")

if sleepy  == "y" or thirsty == "y" and travelling == "y"  and less_money == "y":
    print(" we will help you")
else: 
    print(" You dont need our help")

# y y y n , we have entered these inputs and expexted output is >>>>>>>>>> help you 

if (sleepy == "y" or thirsty == "y" and travelling == "y" ) or (less_money == "y"): #using () to group AND and OR conditions 
    print(" we will help you")
else: 
    print(" You dont need our help")



# UNDERSTANDING BELOW CODE WITH TRUTH VALUES(Important concept)


if 0 : # HERE CONDITION WILL ALWAYS BE FALSE
     print("True")
else: a = int(input(" Guess a number "))
if a == 15 : # there is a chance of this statement to be true if guess is 15 
     print("True")
else:
    print("False")  


a = int(input(" Guess a number greater than 20 "))
if a == 15 :  # there is  no chance of this statement to be true  as the user will always guess num geater than 20
     print("True")
else:
    print("False") 





name1 = int(input(" Guess a number greater than 30 "))
if a == 15 :  # there is  no chance of this statement to be true  as the user will always guess num geater than 20
     print("True")
else:
    print("False") 


name1 = input(" Guess a number greater than 30 ")
if name1:  # if the user does not give any input , it will be an EMPTY string , which makes the condition FALSE always
     print("True")
else:
    print("False") 






# using membership operator in IF conition

even1 = [2,4,6,8]

if 20 in even1:
    print("True ") 
else:
    print("false")


if  6 not in even1:
    print("True ") 
else:
    print("false")

name2 = "Maharashtra"

if  "tra"  in name1:
    print("True") 
else:
    print("false")