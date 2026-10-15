


class BankAccount:
    def __init__(self, balance) -> None:
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

bank = BankAccount(1000)

print(bank.__dict__)
print(bank._BankAccount__balance)
bank._BankAccount__balance = 100000
print(bank._BankAccount__balance)