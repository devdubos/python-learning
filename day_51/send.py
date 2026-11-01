


def command_generator():
    total = 0
    yield "ready"
    number = yield  
    yield number



g = command_generator()

# print(next(g))       
# next(g)
# print(g.send(("add", 100)))



def budget_tracker():
    total = 0
    while True:
        expense = yield total
        total += expense

# tracker = budget_tracker()
# next(tracker)

# print(tracker.send(150))
# print(tracker.send(200))
# print(tracker.send(50))
       



def wallet_generator():
    total = 0
    yield "Кошелек открыт"
    while True:
        coin = yield total
        if coin is not None:
            total += coin

g = wallet_generator()

print(next(g))
print("Баланс:", g.send(50))
print("Баланс:", g.send(100))
print("Баланс:", g.send(25))







def caps_lock_generator():
    yield "Система капслока готова"
    while True:
        text = yield
        if text is not None:
            print("Результат:", text.upper())

g = caps_lock_generator()

next(g)
g.send("привет")
g.send("python")
g.send("работает")