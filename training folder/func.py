def to_jaden_case(string):
    string1= string.split()
    string1 = [i.capitalize() for i in string1]
    string2 = " ".join(string1)
    return string2
    
def to_camel_case(string):
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    return "".join(capitalized_words)

def pig_latin(string):
    words = string.split()
    transformed_words = [word[1:] + word[0] + "ay" for word in words]
    return " ".join(transformed_words)

def filter_list(l):
    result = []
    for i in l:
        if type(i) == int:
            result.append(i)
    return result

def filter_strins(l):
    result = []
    for i in l:
        if type(i) == str: 
            result.append(i)
    return result

def filter_strings(l):
    return [i for i in l if type(i) == str]


def get_even_numbers(l):
    result = []
    for i in l:
        if i % 2 == 0:
            result.append(i)
    return result


user_data = {
    "username": "alex_backend",
    "email": "alex.dev@mail.com",
    "password": "super_secret_pass"
}

# def validate_registration(user_data):
#     name = user_data.get("username")
#     if not name:
#         return {
#             "status":"empty - wrong - error",
#             "message": "Please write correct username"
#         }
#     email = user_data.get("email")
#     if "@" not in email:
#         return {
#             "status":"not found '@'",
#             "message": "Please write valid email"
#         }
#     password = user_data.get("password")
#     if len(password) <= 6:
#         return {
#             "status":"short password",
#             "message": "Please write password more then 6 simbol"
#         }        
#     return {
#         "status":"Valid data, complete",
#         "message":"Success registration"
#     }
    
def validate_registration(user_data):
    if not user_data.get("username"):
        return {
            "status":"empty - wrong - error",
            "message": "Please write correct username"
        }
    if "@" not in user_data.get("email",""):
        return {
            "status":"not found '@'",
            "message": "Please write valid email"
        }
    if len(user_data.get("password","")) <= 6:
        return {
            "status":"short password",
            "message": "Please write password more then 6 simbol"
        }        
    return {
        "status":"Valid data, complete",
        "message":"Success registration"
    }
print(validate_registration(user_data))


catalog = [
    {"name": "Мышка", "price": 450, "category": "Электроника"},
    {"name": "Клавиатура", "price": 1200, "category": "Электроника"},
    {"name": "Коврик", "price": 300, "category": "Аксессуары"},
    {"name": "Наушники", "price": 490, "category": "Электроника"},
    {"name": "Шнур HDMI", "price": 600, "category": "Электроника"}
]




def filtration_price(catalog,max_price,category):
    catalog_filtr = []
    for product in catalog:
        price = product.get("price")
        if price < max_price and category == product.get("category"): 
            catalog_filtr.append(product)
    return catalog_filtr

# Имитируем запрос от Вани: он ищет Электронику до 500 рублей
print(filtration_price(catalog, max_price=500, category="Электроника"))
# Твой бэкенд должен выдать: Мышку (450) и Наушники (490)

# Имитируем запрос от Ани: она ищет Аксессуары до 1000 рублей
print(filtration_price(catalog, max_price=1000, category="Аксессуары"))
# Твой бэкенд должен выдать: Коврик (300)


user_cart = [
    {"name": "Футболка", "price": 1000, "quantity": 2}, # 2 штуки по 1000 = 2000 руб
    {"name": "Кепка", "price": 500, "quantity": 1}      # 1 штука по 500 = 500 руб
]

def promocod_box(user_cart, promocod):
    result_price = 0
    discount = 1
    if promocod == "A3Y6":
        discount = 0.9
    for product in user_cart:
        result_price += product.get("price") * product.get("quantity")
    return result_price * discount










user_cart = [
    {"name": "Футболка", "price": 1000, "quantity": 2}, # 2 штуки по 1000 = 2000 руб
    {"name": "Кепка", "price": 500, "quantity": 1}      # 1 штука по 500 = 500 руб
]


class Cart:
    def __init__(self, items) -> None:
        self.product = items
    def get_final_price(self, promocod):
        result_price = 0
        discount = 1
        if promocod == "A3Y6":
            discount = 0.9
        for product in self.product:
            result_price += product.get("price") * product.get("quantity")
        return result_price * discount

my_cart = Cart(user_cart)
print(my_cart.get_final_price("A3Y6"))






class Cart:
    def __init__(self, items):
        self.product = items 

    def add_product(self, name, price, quantity):
       
        self.product.append({"name": name, "price": price, "quantity": quantity})

    def remove_product(self, name):
     
        self.product = [p for p in self.product if p["name"] != name]

    def get_final_price(self):
        total = 0
        for p in self.product:
            total += p["price"] * p["quantity"]
        return total



y = [{"name": "Футболка", "price": 1000, "quantity": 2}]
x = Cart(y) 


x.add_product("Кепка", 500, 1) 
x.remove_product("Футболка")    


price = x.get_final_price()
print(price) 





class User:
    def __init__(self, username, email, password):
        self.name = username
        self.email = email
        self.password = password
        self.is_blocked = False

    def change_password(self, old_pass, new_pass):
        if self.password == old_pass:
            self.password = new_pass
            return "Пароль успешно изменен"
        return "Старый пароль неверный"

    def block_user(self):
        self.is_blocked = True

    def send_message(self, text):
        if self.is_blocked:
            return "Ошибка: ваш аккаунт заблокирован"
        return f"Пользователь {self.name} отправил сообщение: {text}"

