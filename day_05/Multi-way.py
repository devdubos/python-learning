light_color = "yellow"

if light_color == "red":
    print("Stop!")
elif light_color == "yellow":
    print("Slow down!")
elif light_color == "green":
    print("Go!")
else:
    print("Invalid color!")
    
customer_age = 16
ticket_price = 10 if customer_age < 18 else 15
print(f"Ticket price: ${ticket_price}")

x = int(input())
if x % 2 == 0:
    if 0 <= x <= 9:
        print("x - nubmer")
    else:
        print("x - clock")
else:
    print("not 2/ number")


a = int(input("a: ")) 
b = int(input("b: "))
c = int(input("c: "))
if a > b:
    if a > c:
        print("a -> max")
    else:
        print("c -> max")
else:
    if b > c:
        print("b -> max")
    else:
        print("c -> max")


        