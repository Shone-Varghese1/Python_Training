class person:
    def __init__(self,name):
        self.name=name
class Employee(person):
    def __init__(self,name,emp_id):
        super().__init__(name) #call parent constructor
        self.emp_id=emp_id
e=Employee("Shone",101)
print(e.name,e.emp_id)