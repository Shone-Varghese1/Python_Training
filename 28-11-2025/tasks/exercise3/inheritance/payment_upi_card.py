
class Payment:
    def process(self):
        return "Processing payment..."

class CreditCardPayment(Payment):
    def process(self):
        return "Processing credit card payment..."

class UPIPayment(Payment):
    def process(self):
        return "Processing UPI payment..."

p1 = CreditCardPayment()
p2 = UPIPayment()
print(p1.process())
print(p2.process())
