
#################################################
# USER DEFINED MODULE
#  codewritten in file randomModuleFile2.py
#################################################

def separator():
    print("***********************")
def minus():
    print("---------------------")


def sum1(a, b):
    return a+b


# below lines of code can be accessed inside the file only
# not accessible/visible if imported in another file

# if __name__ == "__main__":
#     print("You are Admin in randomModuleFile2 and password is : Admin@123")

# line no 20 ka meaning ye hai ki agar tum is file me ho tab hi print hona chahiye nahi to import karte samay print nahi hona chahiye  

print(__name__)     #ye is file ka main hai   