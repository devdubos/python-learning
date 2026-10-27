#learn .send()

def echo_generator():
    received = yield "Жду сообщение"
    yield f"Вы прислали: {received}"

g = echo_generator()

print(next(g))
print (g.send("Привет!"))



def pulsar():
    wait = "Signal"
    while True:
        new_wait = yield wait
        if new_wait is not None:
            wait = new_wait
        
p = pulsar()

print(next(p))
print(p.send("new massage"))
print(next(p))


learn .