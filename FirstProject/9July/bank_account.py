class BankAccount:
    def __init__(self,name, balance):
        self.name= name
        self.__balance=balance

    def deposit(self,amount):
        self.__balance=self.__balance+amount
        print("Despited Balance :", self.__balance)

    def withdraw(self, amount):
        self.__balance = self.__balance-amount
        print("Withrdraw Balance :",self.__balance)

    def display_balance(self):
        print("Balance :", self.__balance)

a1=BankAccount("Raj", 1000)
a1._BankAccount__balance=12
a1.deposit(1000)
# a1.withdraw(500)
a1.display_balance()
a1._BankAccount__balance=12
print(a1._BankAccount__balance)
print(a1.__dict__)