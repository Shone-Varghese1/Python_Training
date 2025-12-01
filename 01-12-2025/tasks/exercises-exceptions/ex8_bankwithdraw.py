class LowBalanceError(Exception):
    pass
class Account:
    def __init__(self,acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance
    def withdraw(self,amount):
        if amount > self.balance:
            raise LowBalanceError("Insufficient balance")
        self.balance -= amount
    def print_balance(self):
        print(self.balance)
a1=Account("a1",100)
a1.withdraw(110)
a1.print_balance()


# def withdraw(amount,balance):
#     if amount > balance:
#         raise LowBalanceError("Insufficient funds")
#     return balance-amount
# withdraw(100,10)