from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def processPayment(self):
        pass

class CreditCardPayment(PaymentMethod):
    def processPayment(self):
        print("Credit card payment is being processed")
        return super().processPayment()
    
class PayPalPayment(PaymentMethod):
    def processPayment(self):
        print("PayPal payment is being processed")
        return super().processPayment()  

cc = CreditCardPayment()
pp = PayPalPayment()
cc.processPayment()
pp.processPayment()