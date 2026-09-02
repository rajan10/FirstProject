class BankAccount():
    def __init__(self,balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self,balance):
         self.__balance=balance

account=BankAccount(100)
print(account._BankAccount__balance) # name mangling and tweaking inside how pvt variable are stored
print(account.get_balance()) # getters 
account.set_balance(1000)
print(account.get_balance())



