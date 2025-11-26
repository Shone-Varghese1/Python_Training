class Customer:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def display(self):
        print(self.name)
        print(self.age)
        print(self.city)
    def eligible(self):
        print("Eligible for Loyalty program" if self.age>25 else "Not eligible for Loyalty program")
Customer1=Customer("Shone",22,"Cochin")
Customer2=Customer("Ravi",27,"Alappuzha")
Customer1.display()
Customer1.eligible()
print()
Customer2.display()
Customer2.eligible()