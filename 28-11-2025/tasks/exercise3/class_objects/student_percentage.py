class Student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def total(self ):
        return self.m1+self.m2+self.m3
    def percent(self):
        return (self.total()/300)*100



    def display(self):
        print("name:",self.name)
        print("marks: ",self.m1,self.m2,self.m3)
        print("total:",self.total())
        print("percentage :",self.percent())


s1=Student("shone",85,85,100)
s1.display()