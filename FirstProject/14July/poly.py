class UpiPayment:
    def pay(self,amount):
        print(f"paid {amount} using UPI payment")

class DebitCardpayment:
    def pay(self,amount):
        print(f"paid {amount} using Debit Card")

def make_payment(method, amount):
    """Invoke the payment method's pay() to process the payment."""
    method.pay(amount)


# if __name__ == "__main__":
make_payment(DebitCardpayment(), 1000)