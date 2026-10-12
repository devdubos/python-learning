class User:
    def __init__(self,name:str, age:int) -> None:  
        self.name = name
        self.age = age
        self.is_human = True
    def say_hello(self):
        print(f'Hello, im {self.name}')

user1 = User("Sergey", 24)


class GameCharacter:
    def __init__(self, name, damage, health) -> None:
        self.name = name
        self.damage = damage
        self.health = health
    def attack(self):
        return f"{self.name} did {self.damage} of damage!"
        

        