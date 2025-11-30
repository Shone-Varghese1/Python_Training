
class Vehicle:
    def start(self):
        return "Starting vehicle"

class Car(Vehicle):
    def start(self):
        return "Car running"


c = Car()
print(c.start())
