# 18. Create a Payment class with credit-card and UPI subclasses overriding process_payment()

class Payment:
    def process_payment(self):
        print("process payment")
class CreditCard(Payment):
    def process_payment(self):
        print("process payment in credit card")
class Upi(Payment):
    def process_payment(self):
        print("process payment in upi")
u1=Upi()
u1.process_payment()
c1=CreditCard()
c1.process_payment()
