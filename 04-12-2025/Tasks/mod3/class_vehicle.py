# 19. Create a Vehicle class and Car, Bike subclasses. Override max_speed().
class Vehicle:
    def max_speed(self):
        print("max speed in vehicle")
class Bike(Vehicle):
    def max_speed(self):
        print("max speed is 60km/hr for bike")
class Car(Vehicle):
    def max_speed(self):
        print("max speed is 80km/hr for car")
b1=Bike()
b1.max_speed()
c1=Car()
c1.max_speed()