class UpiPayment:
    def pay(self,amount):
        print(f"Paid {amount} using UPI")

class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class DebitCardPayment:
    def pay(self, amount):
        print(f"Paid {amount} using Debit Card")

class CashPayment:
    def pay(self,amount):
        print(f"paid {amount} using Hand Cash")

def make_payment(payment_method_type, amount):
    payment_method_type.pay(amount)

make_payment(CreditCardPayment(), 1000)
make_payment(DebitCardPayment(), 1000)
make_payment(CashPayment(), 1000)