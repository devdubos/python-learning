import time

# def decorator_timer(func):
#     print("start")
#     func()
#     print("end")
#     return  None


# def load_file():
#     print("Loading file....1...2")
#     time.sleep(2)


# load_file = decorator_timer(load_file) # <---- wrapper



# def decorator_timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Time completed: {(end - start)}")
#         return result
#     return wrapper

# @decorator_timer
# def load_file(seconds):
#     print("Loading file....1...2")
#     time.sleep(seconds)



# load_file(1)
# load_file(0.5)



# @decorator_timer
# def multyply(a, b):
#     print("Initialisating...")
#     time.sleep(1)
#     return a * b
# print(multyply(2,6))
user_id = 42
from functools import lru_cache

@lru_cache
def get_user_heavy_data(user_id):
    time.sleep(2)
    return f"User's data {user_id}"

# print(get_user_heavy_data(user_id))
# print(get_user_heavy_data(user_id))

class User:
    def __init__(self, name:str, surname:str) -> None:
        self.name = name
        self.surname = surname
    @property
    def full_name(self):
        fullname = self.surname +' '+ self.name
        return fullname.upper()
    @staticmethod
    def is_valid_email(email:str) -> tuple[bool,str]:
        if "@" not in email:
            return False, "Error please write valid email"
        if "gmail.com" not in email and "mail.com" not in email and "yandex.com" not in email  and "icloud.com" not in email:
            return False, "Error please write valid email"
        if len(email) > 20:
            return False, "Your email have to be no more letters then 15"
        else:
            return True, "Ur email valid."


print(User.is_valid_email("sergey@gmail.com"))
# user = User("Sergey", "Dubos")

# print(user.full_name)



