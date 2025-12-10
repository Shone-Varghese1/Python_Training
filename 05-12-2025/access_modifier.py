class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner #public
        self.__balance = balance #private attribute
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("invalid deposit amount")
    def withdraw(self,amount):
        if amount <=self.__balance:
            self.__balance -= amount
        else:
            print("insufficient funds")

    def get_balance(self):
        return self.__balance
acc = BankAccount("shiva",5000)
acc.deposit(2000)
print(acc.get_balance())
acc.withdraw(3000)
print(acc.get_balance())
print(acc.owner)
acc.__balance=100000
print(acc.get_balance())
print(dir(acc))