# Create a class Rectangle with methods to calculate area and perimeter.

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def compute_area(self):
        return self.length*self.breadth
    def compute_perimeter(self):
        return 2*(self.length+self.breadth)
r1=Rectangle(10,5)
print(r1.compute_area())
print(r1.compute_perimeter())
