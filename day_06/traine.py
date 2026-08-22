# # multi-way
def task_weight():
    weight = float(input())
    if weight <= 60.0:
        print("light")
    elif weight <= 64.0:
        print("halflight")
    elif weight <= 69.0:
        print("halfmedium")
    else:
        print("other")

def task_age():
    age = int(input())
    if age < 0 or age > 120:
        print("Error uncorrect age")
    elif  0 <= age <= 2:
        print("littlechild")
    elif  3 <= age <= 12:
        print("child")
    elif  13 <= age <= 17:
        print("child")
    elif 18 <= age <= 64:
        print("adult")
    else:
        print("granny")

def task_sum():
    summ = int(input())
    if summ <= 0:
        print("Errro summ too small")
    else:
        if summ < 1000:
            discount_percent = 0
        elif 1000 <= summ < 5000:
            discount_percent = 0.05
        elif 5000 <= summ < 10000:
            discount_percent = 0.10
        else:
            discount_percent = 0.15
        discount_amont = summ * discount_percent
        result_sum = summ - discount_amont
        print(f"{result_sum:.2f}")

def task_minimum():
    a, b, c = map(int,input().split())
    if a < b:
        if a < c:
            print(a)
        else:
            print(c)
    else:    
        if b < c:
            print(b)
        else:
            print(c)

def task_ternarnoper():
    a = 12
    b = 7
    print(1, 2 , a if a < b else b, 4 , 5)

def task_ternarnoper2():
    hours = int(input())
    allsum = hours * 150
    print(f"itogsum: {allsum * 0.8 if hours > 5 else allumm:.2f}")

def task_weight():
    weight = int(input())
    print(f" task delivery: {300 if weight <= 5 else weight * 80:.2f} dollars")

def task_calculator():
    bill = float(input())
    if bill <= 0:
        print("error")
    else:
        task_tips = 0.1 if bill < 2000 else 0.15
        print(f"ur tips: {bill * task_tips}")
task_calculator()

    
    
