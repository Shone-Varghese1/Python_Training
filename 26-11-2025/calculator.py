class Calculator:
    def __init__(self):
        pass
    def add(self,a,b):
        print(f"{a}+{b}={a+b}")
    def sub(self,a,b):
        print(f"{a}-{b}={a-b}")
    def mul(self,a,b):
        print(f"{a}*{b}={a*b}")
    def div(self,a,b):
         try:
            print(f"{a}/{b}={a/b}")
         except :
             print("zero division error")
obj1=Calculator()
obj1.add(1,2)
obj1.sub(5,3)
obj1.mul(2,3)
obj1.div(6,3)
obj1.div(7,0)