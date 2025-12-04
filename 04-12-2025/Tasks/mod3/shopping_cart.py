# 21. Build a ShoppingCart class implementing add, remove, total, apply_discount.

class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self,name,price):
        self.items.append((name,price))
        print("added item")
    def remove_item(self,name):
        for item in self.items:
            if item[0]==name:
                self.items.remove(item)
                print("removed item")
                return
        print("no item found")
    def amount(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total
    def discount(self,percent):
        total=self.amount()
        discount=total*(percent/100)
        final=total-discount
        return final
    def display(self):
        for item in self.items:
            print(item[0],item[1])
s1=ShoppingCart()
s1.add_item("laptop",100000)
s1.add_item("mouse",2000)
s1.add_item("keyboard",5000)
s1.display()
print(s1.amount())
print(s1.discount(5))
s1.remove_item("laptop")
s1.display()




