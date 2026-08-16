number = 100
classification = "Greater than 100" if number > 100 else ("Exactly 100" if number == 100 else "Less than 100")

num1 = 10
num2 = 0
operation = "/"

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    # Handling division by zero
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(num1 / num2)
else:
    print("Unknown operation")