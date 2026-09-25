def withdraw(account_dict: dict, amount: float):
    if account_dict["balance"] >= amount:
        account_dict["balance"] -= amount
        print(f"Withdrew {amount}. New balance: {account_dict['balance']}")
    else:
        print("Insufficient funds!")
alex_account = {
    "owner": "Alex",
    "balance": 1000
}
withdraw(alex_account, 300)



class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

alex_account = BankAccount("Alex", 1000)


alex_account.withdraw(300)