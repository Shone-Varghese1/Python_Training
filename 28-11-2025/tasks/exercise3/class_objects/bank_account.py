class BankAccount:
    def __init__(self,acc_no,acc_holder,balance):
        self.acc_holder=acc_holder
        self.acc_no=acc_no
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"deposited {amount} successfully")
        self.check_balance()
    def withdraw(self,amount):
        if self.balance<amount:
            print("Not enough money")
        else:
            self.balance -= amount
            print(f"withdrawn {amount} successfully")
            self.check_balance()
    def check_balance(self):
        print("balance: ",self.balance)
A1=BankAccount(1,"Shone",5000)
A1.check_balance()
A1.deposit(2000)
A1.withdraw(3000)