class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Error! Insufficient funds to withdraw {amount}. Balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. Remaining balance: {self.balance}")

my_account = BankAccount("Alex", 1000)
my_account.deposit(500)
my_account.withdraw(2000)
my_account.withdraw(700)



class Cart:
    def __init__(self):
        self.items = {} 

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Added '{item_name}' for {price}")

    def get_total(self):
        total_price = sum(self.items.values())
        return total_price

my_cart = Cart()
my_cart.add_item("Shoes", 5000)
my_cart.add_item("T-shirt", 1500)
print(f"Total price: {my_cart.get_total()}")