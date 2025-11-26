class Car:
    def __init__(self,brand,model,price):
       self.brand=brand
       self.model=model
       self.price=price
    def display(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        print("Price: ",self.price)
        print("###################")
car1=Car("honda",'Amaze',1000000)
car2=Car("honda",'City',1100000)
car3=Car("Toyota","fortuner",2700000)
car1.display()
car2.display()
car3.display()

class Employee:
    def __init__(self,emp_id,name,department,salary):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.salary=salary
    def display(self):
        print("Employee ID: ",self.emp_id)
        print("Name: ",self.name)
        print("Department: ",self.department)
        print("Salary: ",self.salary)

#creating employee objects

E1=Employee(1,"Shone","IT",100000)

E2=Employee(2,"Ravi","Sales",75000)

E1.display()
print()
E2.display()

