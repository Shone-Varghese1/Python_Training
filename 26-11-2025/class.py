class Student:
    pass
s1=Student()
s2=Student()
print(s1)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s3=Student("shone",21)
s4=Student("hari",21)
print(s3)
print(s3.name,s3.age)
print(s4.name,s4.age)

