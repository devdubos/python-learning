
#def task_101():
    #balance = 0
    #while balance < 100:
        #balance += 20
    #print(balance)
#task_101()

def learn_while():
    x = int(input())
    box = 0
    while x != 0:
        box += x
        x = int(input())
    print(box)

def learn_while2():
    box = 0
    x1 = 0
    while x1 != 10:
        x1 += 1
        x = int(input())
        if x >= 0:
            box += x
        else:
            print('stop')
            break
    print(box)
learn_while2()

            
        