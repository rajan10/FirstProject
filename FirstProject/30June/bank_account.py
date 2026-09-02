class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

b1=BankAccount(1000)  # Create a bank account with an initial balance of $1000
print(b1)
