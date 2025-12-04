# 17. Implement a Product → ElectronicProduct (inheritance) where Electronics adds warranty years.
class Product:
    def __init__(self,product_id):
        self.product_id = product_id
class ElectronicProduct(Product):
    def __init__(self,product_id,warranty):
        super().__init__(product_id)
        self.warranty = warranty
    def warranty_1(self):
        if self.warranty:
            print("product under warranty")
e1=ElectronicProduct(101,"True")
e1.warranty_1()
