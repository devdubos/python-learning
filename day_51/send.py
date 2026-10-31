


def command_generator():
    total = 0
    yield "ready"
    number = yield  
    yield number
g = command_generator()

print(next(g))       
print(next(g))
g.send(("add", 100))
print(next(g))

       