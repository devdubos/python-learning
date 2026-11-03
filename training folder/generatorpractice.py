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


# N = int(input("Ur number please: "))
# nubmers =range(1, N+1)
# limit = int(input("Ur limit please: "))

# def even_numbers(numbers):
#     for num in nubmers:
#         if num % 2 == 0:
#             yield num

# def square_numbers(start_num):
#     for num in start_num:
#         yield num**2

# def cut_nubmers(square_num, limit):
#     for num in square_num:
#         if num >= limit:
#             return  
#         else:
#             yield num



def read_logs():
    with open("training folder/text.log", encoding="utf-8") as f:
        for line in f:
            yield line.strip()

def parse_to_dict(line):
    




g = read_logs()
g2 = parse_to_dict(g)
g3 = None
