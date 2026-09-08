def task_evenodd():
    num = int(input("Ur number: "))
    if num % 2 == 0:
        print ("even number")
    else:
        print("Odd number")

def task_sunny():
    is_sunny = True
    is_weekend = True
    if is_sunny == True and is_weekend == True:
        print("Perfect day for a walk")
    elif is_sunny == True and is_weekend == False:
        print("Perfect wheather but u need work")
    elif is_sunny == False and is_weekend == True:
        print("U can stay home and rest")
    else:
        print("Work day with bad whether")


def task_ternarn():
    age = int(input("Write ur age: "))
    status = "elder" if age >= 40 else "young"
    print(status)


def task_ternarn1212():
    age = int(input("Write ur age: "))
    return "Access true" if age >= 18 else "Access false"
print(task_ternarn1212())

def task_price():
    price = 500
    balance_card = float(input("Write balance of ur card: "))
    return "Buying true" if balance_card >= price else "Buying false"
print(task_price)

def task_temp():
    temp = float(input("Write temperature: "))
    return "Boyling" if temp >= 100 else ("Frizze" if temp <= 0  else "liqud")
print(task_temp())