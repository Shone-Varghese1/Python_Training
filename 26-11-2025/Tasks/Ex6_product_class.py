class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def total_cost(self):
        return self.price*self.quantity
    def checkout(self):
        print(f" The cost for  {self.quantity} {self.name}s is {self.total_cost()}")


product1=Product("pen",5,10)
product2=Product("Marker",20,3)
product1.checkout()
product2.checkout()

