class Company:
    def __init__(self,company_name,location):
        self.company_name = company_name
        self.location = location
class Employee(Company):
    def __init__(self,emp_name,emp_id,company_name,location):
        super().__init__(company_name,location)
        self.EmployeeName = emp_name
        self.EmployeeID = emp_id
e1=Employee("Shone",100,"EY","Kochi")
print(e1.EmployeeName)
print(e1.EmployeeID)
print(e1.company_name)
print(e1.location)
