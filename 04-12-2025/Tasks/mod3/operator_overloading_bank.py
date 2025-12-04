# 20. Implement Operator Overloading: add two objects of BankAccount to return total balance.
class BankAccount:
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.balance = balance
    def __add__(self,other):
        return self.balance + other.balance
a1=BankAccount(101,1000)
a2=BankAccount(102,5000)
print(a1+a2)
