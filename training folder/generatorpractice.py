#learn .send()

def echo_generator():
    received = yield "Жду сообщение"
    yield f"Вы прислали: {received}"

# g = echo_generator()

# print(next(g))
# print (g.send("Привет!"))



def pulsar():
    wait = "Signal"
    while True:
        new_wait = yield wait
        if new_wait is not None:
            wait = new_wait
        
# p = pulsar()

# print(next(p))
# print(p.send("new massage"))
# print(next(p))


N = int(input("Ur number please: "))
nubmers =range(1, N+1)
limit = int(input("Ur limit please: "))

def even_numbers(numbers):
    for num in nubmers:
        if num % 2 == 0:
            yield num

def square_numbers(start_num):
    for num in start_num:
        square = num**2
        yield square

def cut_nubmers(square_num, limit):
    for num in square_num:
        if num >= limit:
            return num and "processing compelete"
        else:
            yield num
        return "processing compelete"


start_num = even_numbers(nubmers)
square_num = square_numbers(start_num)
limit_num = cut_nubmers(square_num, limit)


while True:
    try
    num = next(limit_num)
    if not num:
        break
    print(num)