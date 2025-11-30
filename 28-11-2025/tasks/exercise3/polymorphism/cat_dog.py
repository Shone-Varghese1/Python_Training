# Create two classes Cat and Dog. Both should have a method sound() that behaves differently.
class Cat:
    def sound(self):
        return "meow"
class Dog:
    def sound(self):
        return "woof"
c1=Cat()
d1=Dog()
print(c1.sound())
print(d1.sound())
