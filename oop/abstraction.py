from abc import ABC, abstractmethod


class GateWay(ABC):
    @abstractmethod
    def pay(self):
        pass

class RazorPay(GateWay):
    def pay(self):
        print("paying using razor pay")

class PayPal(GateWay):
    def pay(self):
        print("paying using PayPal")

class Purchase:
    def __init__(self, gateway):
        self.gateway = gateway
        
    def checkout(self):
        print("checking out...")
        self.gateway.pay()
    

gateway1 = RazorPay()
gateway2 = PayPal()
purchase = Purchase(gateway2)
purchase.checkout()        