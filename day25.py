
#Exception in python
#using valueError in the code for warning user that length of text is out of banner

def banner_text(text): #using single parameter

    screen_width =200
    if len(text)>screen_width-4:
        raise ValueError("Lengthy String")# we will raise value error with comments passed in the argument

    if text =="*":
         print("*"*screen_width)
    else:
        center_text = text.center(screen_width-4)
        print("**{}**".format(center_text))

banner_text("*")
banner_text("")# using keyword to specify the parameter using in the argument
banner_text("WE,THE PEOPLE OF INDIA,having solemnly resolved to constitute India into a SOVEREIGN,DEMOCRATIC,SOCIALIST SECULAR,DEMOCRATIC,REPUBLIC and to secure to all its citizens;")
banner_text("JUSTICE,social,economic and political;")
banner_text("LIBERTY of thought,expression,belief,faith and worship;")
banner_text("EQUALITY of status and of opportunity;and to promote among them all")
banner_text("FRATERNITY assuring the dignity of the individual and the unity of the Nation,")
banner_text("IN OUR CONSTITUENT ASSEMBLY this twenty-sixth day of November,1949,do HEREBY ADOPT,ENACT AND GIVE TO OURSELVES THIS CONSTITUTION ")
banner_text("*")


# exception in python
#using ZeroDivvvvvvvvvvvvvvvvvvnError explicitly to warn the user

# def div1(a,b):
#     if b==0:
#         raise ZeroDivisionError("The deno is ZERO Please do not use zero in b")
#     else:
#         c=a/b
#         return c
# ans1=div1(15,0)
# print(ans1)            

# Type of parameters in Python

def func(p1,p2,*args,p5):
    print("Position arguments / Keyword p1:{},p2:{},p5{}".format(p1,p2,p5))
    print(type(p1))
    print(type(p2))
    print("Var arguments *args {}".format(args))
    print(type(args))
func(1,2,5,55,555,5555,p5=6) #here p5 is keyword argument used after variable argument to separate from *args    