# 16. Build a Student class storing id, name, and marks. Add methods to calculate grade.
# 17. Implement a Product → ElectronicProduct (inheritance) where Electronics adds warranty years.

# 19. Create a Vehicle class and Car, Bike subclasses. Override max_speed().
# 20. Implement Operator Overloading: add two objects of BankAccount to return total balance.
# 21. Build a ShoppingCart class implementing add, remove, total, apply_discount.
#
# 22. Create a Library class to store books and a method to search by title or author.
# 23. Create a User class and an Admin subclass that can delete a user (override methods).

class Student:
    def __init__(self, name,student_id,marks):
        self.name = name
        self.student_id = student_id
        self.marks = marks
    def grade(self):
        total=0
        for mark in self.marks:
            total+=mark
        total /= 5

        if total>=90:
            return 'A'
        elif total>=80:
            return 'B'
        elif total>=70:
            return 'C'
        elif total>=60:
            return 'D'
        else:
            return 'F'
s1=Student("Shone",101,[95,75,86,89,91])
print(s1.grade())
