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

