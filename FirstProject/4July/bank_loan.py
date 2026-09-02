class LoanAccount:
    def __init__(self, account_number, account_holder, loan_id, interest_rate=13, loan_amount=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.loan_id = loan_id
        self.interest_rate = interest_rate
        self.loan_amount = loan_amount

    def take_loan(self, amount):
        if amount<=0:
            return False, "Invalid loan amount"
        
        print("Original Loan Amount:", self.loan_amount)
        self.loan_amount=self.loan_amount+amount
        return True, f"After adding ${amount} of loan, the loan amount is now ${self.loan_amount}"
    
    def calculate_interest(self):
        interest = (self.loan_amount * self.interest_rate) / 100
        return interest
    
    def calculate_total_amount(self):
        total_amount = self.loan_amount + self.calculate_interest()
        return total_amount

    def repay_loan(self, amount):
        total_due=self.calculate_total_amount()
        if amount<=0:
            return False, "Invalid repayment amount"
        if amount >= total_due:
            return True, f"After payment of ${amount}, the loan is fully repaid. Now the balance is ${amount- total_due}"
        if amount < total_due:
            self.loan_amount = total_due- amount
            return  True,f" After paying ${amount}, Partial Loan repayment successful. Remaining loan amount is ${self.loan_amount}"
 
    
    
        
l1=LoanAccount("123456", "John Doe", "LN001", 13, 1000)
success, msg = l1.take_loan(500)
print(msg)
print("Total Amount to be Repaid:", l1.calculate_total_amount())
success, msg=l1.repay_loan(1000)
print(msg)


# print(l1.get_loan_amount())