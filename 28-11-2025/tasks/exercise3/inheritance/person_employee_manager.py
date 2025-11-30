class Person:
    def __init__(self,name):
        self.name = name
class Employee(Person):
    def __init__(self,name,emp_id):
        super().__init__(name)
        self.emp_id = emp_id
class Manager(Employee):
    def __init__(self,name,emp_id,no_of_employees_in_charge_of):
        super().__init__(name,emp_id)
        self.no_of_employees_in_charge_of = no_of_employees_in_charge_of
m1=Manager(name="Shone",emp_id=1,no_of_employees_in_charge_of=3)
print(m1.name,m1.emp_id,m1.no_of_employees_in_charge_of)

