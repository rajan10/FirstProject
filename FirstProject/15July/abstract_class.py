from abc import ABC, abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    def payment_success(self):
        print("payment successful")

class UpiPayment(Payment):
    def pay(self,amount):
       print("paid using UPI :",amount)
       super().payment_success()


class CreditCardPayment(Payment):
    def pay(self,amount):
       print("paid using Credit Card :",amount)

payment_type=UpiPayment()
payment_type.pay(100)