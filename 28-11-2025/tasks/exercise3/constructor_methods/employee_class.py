# Create a class Employee with constructor and method to print details.
class Employee:
    def __init__(self,name,emp_id,pay):
        self.name = name
        self.emp_id = emp_id
        self.pay = pay
    def display_details(self):
        print("name:",self.name)
        print("id:",self.emp_id)
        print("pay:",self.pay)
e1=Employee("Shone",101,75000)
e1.display_details()