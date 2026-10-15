class Employee:    
    def __init__(self,name:str, salary:int) -> None:
        self.name = name
        self.salary = salary
    def work(self):
        print(f"{self.name} working")

class TesterQA(Employee):
    def work(self):
        print(f"{self.name} testing code")   

tester = TesterQA("Sanya", 140)
tester.work()


class Developer(Employee):
    def __init__(self,language:str, **kwrgs):
        super().__init__(**kwrgs)
        self.language = language

    def work(self):
        print(f"{self.name} write code on {self.language}")

class Designer(Employee):    
    # def __init__(self,name, salary) -> None:
    #     self.name = name
    #     self.salary = salary    

    def work(self):
        print(f"{self.name} draw interface")


developer = Developer(name="Sergey", salary=240, language="python")
developer.work()
designer = Designer("Alina",230)
designer.work()