class User:
    def __init__(self,name:str, age:int) -> None:  
        self.name = name
        self.age = age
        self.is_human = True
    def say_hello(self):
        print(f'Hello, im {self.name}')

user1 = User("Sergey", 24)


class GameCharacter:
    def __init__(self, name:str, damage:int, health:int) -> None:
        self.name = name
        self.damage = damage
        self.health = health
    def attack(self):
        return f"{self.name} did {self.damage} of damage!"
    def take_damage(self,amount:int):
        self.health = self.health - amount
        if self.health < 0:
            self.health = 0
        return f"{self.name} got {amount} of damage. He have health:{self.health}hp"

# charater = GameCharacter("Kez", 30, 100 )

# charater.take_damage(30)
# charater.take_damage(30)
# print(charater.take_damage(30))
        

class Cart:
    def __init__(self,owner:str) -> None:
        self.owner = owner     
        self.items = []
    def add_item(self, name:str, price:float):
        self.items.append({
            "name":name,
            "price":price
        })
        return self.items
    def get_total(self):
        total_price = 0
        for item in self.items:
            total_price += item.get("price", 0)
        return total_price
    def __str__(self):
        if not self.items:
            return "Cart empty"
        check_cart =[]
        for item in self.items:
            check_cart.append(f"{item.get("name",0)} - {item.get("price",0)}")
        return "\n".join(check_cart)
test_class = Cart("Admin")
test_class.add_item("Apple",3.5)
test_class.add_item("Banana",4.5)
test_class.add_item("Banana",4.5)
print(test_class.get_total())
print(test_class)          

      








