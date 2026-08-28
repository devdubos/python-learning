def task_1():
    for i in range(3):
        print(f"{i} hello world", end=" ")
def task_2():
    for i in range(11):
        if i % 2 == 0:
            if i < 10:
                print(i, end="-")
            else:
                print(i)

def task_prices():
    prices = [100, 250, 50, 400]
    total = 0 
    for i in prices:
        total = i + total
    print(total)
task_prices()

def task_3():
    secret = "h-e-l-l-o"
    for i in secret:
        if i == "-":
            continue
        else:
            print(f"{i}", end="")
task_3()