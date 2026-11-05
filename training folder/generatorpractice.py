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



def read_lines():
    with open("training folder/text.log", encoding="utf-8") as f:
        for line in f:
            clear = line.strip()
            if clear:
                yield clear

def map_to_dict(line):
    keys = ["user_id", "action", "timestamp", "ip"]
    for item in line:
        item = dict(zip(keys, item.split("|")))
        yield item
 
def security_filter(dictionary:dict):
    for item in dictionary:
        if item.get("action") != "ERROR" and item.get("ip") != "unknown":
            yield item
    
def add_session_metrics(dictionary_generator):
    box = 0
    for item in dictionary_generator:
        if item.get("action") == "PURCHASE":
            item["is_purchase"] = True
        yield item
        box += 1
    else:
        item["is_purchase"] = False
    print(f"Count of all complteted purchases: {box}")
    

# g = read_lines()
# g2 = map_to_dict(g)
# g3 = security_filter(g2)
# g4 = add_session_metrics(g3)

# for item in g4:
#     print(item)


def get_clean_lines():
    with open("training folder/text2.log", "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if clean_line:
                yield clean_line.split("|")



def convert_to_dict(line):
    keys = ["id", "category", "price", "status", "city"]
    for item in line:
        item = dict(zip(keys, item))
        item["price"] = int(item["price"])
        yield item


def audit_filter(convert_to_dict_item):
    for item in convert_to_dict_item:
        if item.get("status") == "completed" and item.get("price") > 0 and item.get("city") != "unknown" and item.get("category")!= "":
            yield item

def add_tax_and_count(item_audit_filter):
    box = 0
    for item in item_audit_filter:
        item["tax"] = float(item.get("price")*0.1)
        box += item.get("price")
        yield item
    print(f"Summ of all deals: {box}")


g = get_clean_lines()
g2 = convert_to_dict(g)
g3 = audit_filter(g2)
g4 = add_tax_and_count(g3)

for item in g4:
    print(item)