# def draw_simbol(text, count):
#     print(text * count)
# draw_simbol('*', 5)
# draw_simbol('!', 2)

def print_ticket(name, film):
    print(f"Ticket for {name} on movie '{film}'!")

print_ticket("Sergey", "Mister and missis Smith")
print_ticket("Julie","Mister and missis Smith" )
print_ticket("Alina","Mister and missis Smith" )



def duble(number):
    result = number * 2   #Rule las vegas) what happend in LA, always keep in LA. Good analogy i never forget this ^)
    return result
primer = 5
print(duble(primer))

def check_number(number):
    if number > 0:
        return 'Positive'
    elif number < 0:
        return 'Negative'
    else:
        return 'Zero'
    
print(check_number(0))



def show_double(x):
    return  x * 2
result = show_double(5)
print(result)

def calculate_area(width, height):
    return width * height

def is_even(number):
    return number % 2 == 0

def get_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def greet_user(name):
    return f"Hello, {name}!"

print(calculate_area(5, 10))
print(is_even(7))
print(get_largest(10, 25, 15))
print(celsius_to_fahrenheit(25))
print(greet_user("Alice"))