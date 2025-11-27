class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def bark(self):
        print("Dog  barks")
d=Dog()
d.speak() #inherited child can access method of parents
d.bark()