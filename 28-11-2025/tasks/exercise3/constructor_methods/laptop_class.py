# Create a class Laptop with constructor taking brand, RAM, price, and method to calculate
# discount.
class Laptop:
    def __init__(self,brand,model,ram,price):
        self.brand = brand
        self.model = model
        self.ram = ram
        self.price = price
    def cal_discount(self,discount):
        return self.price-(self.price*(discount/100))
l1=Laptop("Lenova","loq",16,90000)
print(l1.cal_discount(10))
