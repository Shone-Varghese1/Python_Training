class BankAccount:
    def __init__(self,acc_no,acc_holder,balance):
        self.acc_holder=acc_holder
        self.acc_no=acc_no
        self.balance=balance
        self.transactions=[]
    def deposit(self,amount):
        self.balance+=amount
        str1= f"deposited {amount} successfully current balance is {self.balance}"
        self.transactions.append(str1)
    def withdraw(self,amount):
        if self.balance<amount:
            print("Not enough money")
        else:
            self.balance -= amount
            str2=f"withdrawn {amount} successfully current balance is {self.balance}"
            self.transactions.append(str2)
    def check_balance(self):
        print("balance: ",self.balance)
    def show_transactions(self):
        for log in self.transactions:
            print(log)
A1=BankAccount(1,"Shone",5000)
A1.check_balance()
A1.deposit(2000)
A1.withdraw(3000)
A1.show_transactions()
