class Score:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        if isinstance(other,Score):
            return Score(self.value+other.value)
        return "error"
    def __gt__(self, other):
        if isinstance(other,Score):
            return self.value>other.value
        return "error"

    def __str__(self):
        return f"{self.value}"


s1=Score(100)
s2=Score(200)
print(s1+s2)
print(s1>s2)