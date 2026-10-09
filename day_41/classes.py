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

user_scooter = {
    "id": "045", "model": "Xiaomi","charge":100,"user": "None"
}

class Scooter:
    def __init__(self,items) -> None:
        self.product = items
    def start_ride(self):
        if self.product.get("charge") < 20 or self.product.get("user") == "Yes":
            return {"report message": "None", "user.message":"Error. Please take another scooter."}
        self.product["user"] = "Yes"
        return self.product
    def end_ride(self, time):
        result_money = time * 10
        result_charge = self.product.get("charge") - (time*2)
        self.product.update(charge=result_charge,user = "None")
        return result_money,self.product
    def charge(self):  
        self.product.update(charge = 100)
        return self.product


ride_user_scooter = Scooter(user_scooter)

print("Исходный статус:", user_scooter["user"])


print("\n--- Запускаем start_ride() ---")
print(ride_user_scooter.start_ride()) 



print("\n--- Запускаем end_ride() ---")
print(ride_user_scooter.end_ride(20))



user_data = {
    "name": "Алексей",
    "balance": 1000,          # Деньги на счету для покупки фильмов
    "subscription": "free",   # Может быть "free", "premium" или "admin"
    "history": []             # Список просмотренных фильмов (пока пустой)
}


class UserProfile:
    def __init__(self,user_data) -> None:
        self.data = user_data
    def watch_movie(self, movie_name, is_premium):
        if is_premium == True and self.data.get("subscription")=="free":
            return "error, for watch this movie u need subs"
        if is_premium == False or self.data.get("subscription")=="premium" or self.data.get("subscription")=="admin":
            self.data.update("history").append(movie_name)




