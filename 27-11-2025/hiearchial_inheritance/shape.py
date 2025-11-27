import math


class Shape:
    def __init__(self,no_of_sides):
        self.no_of_sides = no_of_sides
class Rectangle(Shape):
    def __init__(self,no_of_sides,length,breadth):
        super().__init__(no_of_sides)
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
class Circle(Shape):
    def __init__(self,no_of_sides,radius):
        super().__init__(no_of_sides)
        self.radius = radius
    def area(self):
        return math.pi*self.radius**2
class Triangle(Shape):
    def __init__(self,no_of_sides,base,height):
        super().__init__(no_of_sides)
        self.base = base
        self.height = height
    def area(self):
        return self.base*self.height*0.5
c1=Circle("none",5)
t1=Triangle(3,12,3)
r1=Rectangle(4,20,4)

print(c1.no_of_sides,round(c1.area()))
print()
print(t1.no_of_sides,t1.area())
print()
print(r1.no_of_sides,r1.area())