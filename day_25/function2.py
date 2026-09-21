def print_sergey():
    birth_year = 2002
    Name = "Sergey"
    print('Sergey was bor in', birth_year)
    print(f"LOCAL VIEW print_sergey: {locals()}")

print_sergey()

city = 'Moscow'

def show_city():
    city = 'London'
    print(city)

show_city()
print(city)

def draw_line(symbol, count):
      print (symbol * count)

draw_line(symbol= '*' , count= 20)

def draw_line2(symbol, count = 10):
    print(symbol * count)
draw_line2('*')
draw_line2('*',3)

# def sum(*args):
#     total_sum = 0
#     for i in args:
#         total_sum += i       
#     return total_sum

# print(sum(1, 2, 3, 4, 5))
# print(sum(1, 2, 3))
        

def get_sum(*args):
    total_sum = sum(args)
    return total_sum

print(get_sum(1, 2, 3, 4, 5))
print(get_sum(1, 2, 3))
     


def print_info(*args, **kwargs):
    print(kwargs.get('city'))
    print(*args)

print_info(25, 35, counry = 'Belarus',  city = 'Minsk', choice = 'man')

def get_average(*args):
    return sum(args) / len(args) 
print(get_average(1,3,4,5,6))

def calculate_total(price: int, quantity: int, has_discount: bool) -> float:
    total = price * quantity

    if has_discount:
        total -= 10
    return total

