user_cart = [
    {"name": "Футболка", "price": 1000, "quantity": 2, "role": "user" }, # 2 штуки по 1000 = 2000 руб
    {"name": "Кепка", "price": 500, "quantity": 1, "role": "user"}      # 1 штука по 500 = 500 руб
]
vip_cart = [
    {"name": "Куртка", "price": 5000, "quantity": 1, "role": "vip"},
    {"name": "Кроссовки", "price": 4000, "quantity": 1, "role": "vip"}
]
admin_cart = [
    {"name": "Айфон тестовый", "price": 100000, "quantity": 1, "role": "admin"}
]

from typing import List

class Card_box:
    def __init__(self,user_cart: List) -> None:
        self.product: List= user_cart
    def promocod_box(self, promocod):
        discount = 1
        result_price = 0
        if promocod == "A3Y6":
            discount = 0.9
        for product in self.product:               
            result_price += product.get("price") * product.get("quantity")
        return result_price * discount  
    def vip_box(self):
        result_price = 0
        for product in self.product:               
            result_price += product.get("price") * product.get("quantity") * 0.8
        return result_price
    def admin_box(self):
        self.product = []
        return f"Test completed ur worth {self.product}"

mine_card = Card_box(user_cart)
mine_vip = Card_box(vip_cart)
mine_admin = Card_box(admin_cart)

print(mine_card.promocod_box("A3Y6"))
print(mine_card.promocod_box(""))
print(mine_vip.vip_box())
print(mine_admin.admin_box())



def promocod_box(user_cart, promocod):
    result_price = 0
    discount = 1
    if promocod == "A3Y6":
        discount = 0.9
    for product in user_cart:
        result_price += product.get("price") * product.get("quantity")
    return result_price * discount














class Bank:
    def __init__(self,holder,balance) -> None:
        self.holder = holder
        self.balance = balance
    def pay(self, amount):
        result = self.balance - amount
        self.balance
        self.balance = result
        return f"Здравствуйте,{self.holder}. Оплата на сумму {amount} прошла успешна, остаток на счете составляет:{result}"
    def top_up(self, amount):
        result = self.balance + amount
        self.balance = result
        return f"Здравствуйте,{self.holder}. Поступление на карту {amount} прошла успешна, остаток на счете составляет:{result}"

my_card = Bank("Алексей",5000)
# print(my_card.pay(1500))