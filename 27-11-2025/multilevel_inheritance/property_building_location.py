class Property:
    def __init__(self,location):
        self.location = location
class Building(Property):
    def __init__(self,location,no_of_floors):
        super().__init__(location)
        self.no_of_floors = no_of_floors
class Apartment(Building):
    def __init__(self,location,no_of_floors,apartment_id):
        super().__init__(location,no_of_floors)
        self.apartment_id = apartment_id
a1=Apartment("Ernakulam",3,1)
print(a1.location,a1.no_of_floors,a1.apartment_id)

