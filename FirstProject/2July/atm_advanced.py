class ATM:
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return False, "Invalid deposit amount"
        print(f"Original Balance:{self.balance}")
        self.balance += amount
        return True, f"Deposited:{amount}"

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Invalid withdrawal amount"

        if amount > self.balance:
            return False, "Insufficient balance"
        print(f"Original Balance: {self.balance}")
        self.balance -= amount
        return True, f"Withdrawn:{amount}"

    def get_balance(self):
        return self.balance
    
atm = ATM("John", "123", 100)

success, msg = atm.deposit(50)

print(msg)
print("Balance:", atm.get_balance())

# success, msg = atm.withdraw(30)
# print(msg)
# print("Balance:", atm.get_balance())