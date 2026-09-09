def task_01():
    languages = ["Python", "Java", "C++", "JavaScript"]

    for index, lang in enumerate(languages):
        print(f"Index: {index}, Language: {lang}")
#task_01()

def task_02():
    students = ["Alex", "Mary", "John"]
    for table_num, name in enumerate(students, start=1):
        print(f"Table №{table_num}: {name}")
#task_02()

def task_03():
    names = ["Alice", "Bob", "Charlie", "David", "Eva"]

    for index, name in enumerate(names):
        if index % 2 == 0:
            print(f"Even index {index}: {name}")
#task_03()

def task_04():
    steps_per_day = [4500, 11000, 7200, 13500, 3100]
    for idex,steps in enumerate(steps_per_day):
        if steps >= 10000:
            print(f"Day{idex+1} U complete normal! Steps: {steps}") 

def task_05():
    prices = [1500, 450, 3000, 100, 850]
    suma = 0
    for i in prices:
        suma += i
    print(f"total suma: {suma}")

def task_06():
    prices = [1500, 450, 3000, 100, 850]
    box = 0
    for i, price in enumerate(prices):
        if price > 1000:
            box += price
            print(f"Stuf number {i+1} worth more then 1000")
    print(f"Price of all stufs:{box} dollars")
task_06()