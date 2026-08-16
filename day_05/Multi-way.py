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