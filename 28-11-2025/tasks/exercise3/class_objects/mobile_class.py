class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display_details(self):
        print("brand: ",self.brand)
        print("model: ",self.model)
        print("price: ",self.price)
m1=Mobile("Samsung","galaxy s24","42000")
m1.display_details()
