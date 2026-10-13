class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")

class TesterQA(Employee):
    def work(self):
        print(f"{self.name} is testing the application") 

tester = TesterQA(name="Daniil", salary="300k")
tester.work()

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        print(f"{self.name} attacks with a basic strike")

class Wizard(Character):
    def attack(self):
        print(f"{self.name} casts a Fireball")

warrior = Character("Conan", 100)
mage = Wizard("Gandalf", 60)

warrior.attack()
mage.attack()