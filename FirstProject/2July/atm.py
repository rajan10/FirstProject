class ATM:
    def __init__(self, account_holder_name, account_number, balance=0):
        self.account_holder_name = account_holder_name
        self.account_number=account_number
        self.balance = balance

    def display_account_info(self):
       return {
            'Account Holder': self.account_holder_name,
            "Account Number": self.account_number,
            "Balance": self.balance
        }
        
    def check_balance(self):
        if self.balance < 0:
            return "Your account is overdrawn."
        elif self.balance == 0:
            return "Your account balance is zero."
        else:
            return f"Your account balance is {self.balance}."

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        else:
            print(f" Original Balance is {self.balance}")
            self.balance = self.balance + amount
            print(f" New Deposited Amount {amount}")
            print(f" New Balance is {self.balance}")    
    
    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        elif amount > self.balance:
            return "Insufficient funds for withdrawal."
        else:
            print(f" Original Balance is {self.balance}")
            self.balance = self.balance - amount
            print(f" New Withdrawn Amount {amount}")
            print(f" New Balance is {self.balance}")
            
myATM=ATM("John Doe", "123456789", 100)
myATM.deposit(50)
display_account_info = myATM.display_account_info()
print(display_account_info)

# myATM.withdraw(30)
# myATM.display_account_info()
