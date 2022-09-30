#################################################
# decorators
# *****property
# *****getter 
# ****setter
# deleter
#################################################


# class Employee:
#     def _init_(self,salary = 10000):
#         # self.salary = salary # noramal variable
#         # self._salary = salary # Protected  variable only symbolic
#         self.__salary = salary # Private  variable only symbolic

#     def get_salary(self):
#         return self.__salary

#     def set_salary(self,amount):
#         self.__salary = amount
         

# obj1 =  Employee()
# # print(obj1.salary)
# # print(obj1._salary) # AttributeError if accessed directly


# # we are defining a method to access the private variable 
# # encapsulation
# print(obj1.get_salary())

# obj1.set_salary(20000)

# print(obj1.get_salary())

# # print(dir(obj1))
# print("" 30)
# print(obj1.Employee_salary) # actual variable got modified 




 
#################################################
# ****property ****getter
# ****setter
#################################################





class Employee:
    def _init_(self,salary = 10000):
        self.__salary = salary # Private  variable only symbolic


    @property #getter
    def salary(self):
        return self.__salary

    @salary.setter # name of the method and then use .setter
    def salary(self,amount):
        self.__salary = amount
         

obj1 =  Employee()
print(obj1.salary) # attribute , variable : Encapsulation - Hidden 

obj1.salary = 45000

print("The modified Salary as below :")
print(obj1.salary)