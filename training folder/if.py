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
task_sunny()
