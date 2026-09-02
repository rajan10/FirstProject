from abc import ABC, abstractmethod
class Payment(ABC):
    def __init__(self):
        print("Abstract constructor")
    @abstractmethod
    def pay(self, amount):
        pass
    def payment_success_msg(self):
        print("Payment successful!")
class UpiPayment(Payment):
    def __init__(self):
        print("UPI payment constructor")
    def pay(self,amount):
        print("Paid using UPI : " ,amount)
        super().payment_success_msg()
class CreditCardPayment(Payment):     
    def pay(self,amount):
        print("Paid using CreditCard : ", amount)
        super().payment_success_msg()

cc= CreditCardPayment()
cc.pay(200)

# CreditCardPayment