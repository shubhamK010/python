#######################################################################      
##################     SBI                 ############################
#######################################################################
# If the inital balance is not zero 
import datetime

class Account:

    @staticmethod #decorator 
    def current_time():
        return datetime.datetime.now()


    def _init_(self,name,balance): # constructor 
        self.name = name
        self.balance = balance
        # print(" Accont created for " + self.name + " with balance " + self.balance)
        # print(" Accont created for  {} with  balance {}".format(self.name ,self.balance))
        # more readable 
        print(" Accont created for  {0.name} with  balance {0.balance}".format(self))
        self.transaction_list = [(Account.current_time(),balance)] # (when ? ,amount deposited ? )
    def deposit(self,amount):
        amount > 0
        # self.balance = self.balance + amount
        self.balance += amount
        self.show_balance()
        self.transaction_list.append((Account.current_time(), amount))
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("You have insufficien balance for this transaction")
        self.show_balance()
        self.transaction_list.append((Account.current_time(), -amount))
    def show_balance(self):
        print("Balance is Rs. {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list: # unpacking the tuple
            if amount > 0 :
                trans_type = " deposited"
            else:
                trans_type = " withdrawn"
                # amount = amount*(-1)
                amount*=-1

            print("Rs. {} is {}  on {}".format(amount,trans_type,date))


# sharmila = Account("Sharmila",0) #initialised the object
# sharmila.deposit(10000)
# # sharmila.show_balance()
# # sharmila.withdraw(5000)
# # sharmila.show_balance()
# # sharmila.withdraw(50000)
# # sharmila.show_balance()
# sharmila.show_transactions()
# # import time
# # time.sleep(5)
# sharmila.deposit(50000)
# sharmila.show_transactions()
# sharmila.withdraw(50000)
# sharmila.show_balance()
# sharmila.show_transactions()

vivek = Account("Vivek" , 1000)
vivek.show_balance()
vivek.deposit(1000)
vivek.withdraw(500)
vivek.show_transactions()
vivek.show_balance()