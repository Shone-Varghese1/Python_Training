class LowBalanceError(Exception):
    pass
def withdraw(amount,balance):
    if amount > balance:
        raise LowBalanceError("Insufficient funds")
    return balance-amount
withdraw(100,10)