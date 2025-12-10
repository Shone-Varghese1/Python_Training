class Account:
    def __init__(self,acc_no,acc_holder,branch):
        self.acc_no=acc_no
        self.acc_holder=acc_holder
        self.branch=branch
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            print("Not enough money")
        else:
            self.balance-=amount
    def print_balance(self):
        print(self.balance)
class SavingsAccount(Account):
    def __init__(self,acc_no,acc_holder,branch):
        Account.__init__(self,acc_no,acc_holder,branch)
class CurrentAccount(Account):
    def __init__(self,acc_no,acc_holder,branch):
        Account.__init__(self,acc_no,acc_holder,branch)
class SalaryAccount(Account):
    def __init__(self,acc_no,acc_holder,branch):
        super().__init__(acc_no,acc_holder,branch)
s1=SavingsAccount(1,"Ravi","edapally")
c1=CurrentAccount(3,"Hari","Aluva")
Sa1=SalaryAccount(5,"Mohan","Kakkanad")
print(s1.acc_no,s1.acc_holder,s1.branch)
print()
print(c1.acc_no,c1.acc_holder,c1.branch)
print()
print(Sa1.acc_no,Sa1.acc_holder,Sa1.branch)

s1.deposit(100)
s1.withdraw(20)
print("**********")
s1.print_balance()