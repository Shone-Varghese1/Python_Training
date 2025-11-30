class Temperature:
    def __init__(self,value,unit):
        self.value=value
        self.unit=unit
    def to_fahrenheit(self):
        if self.unit=="C":
            return (self.value * 9 / 5) + 32
        else:
            return "invalid operation"

    def to_celsius(self):
        if self.unit=="F":
            return (self.value-32)*5/9
        else:
            return "invalid operation"

t1=Temperature(37,"C")
print(t1.to_fahrenheit())
t2=Temperature(98,"F")
print(t2.to_celsius())