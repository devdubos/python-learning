a = float(input("First number: "))
b = float(input("Second number: "))
operation = input("Choose: ")             
if operation == "+":
    print (f"{a} + {b} = {a + b}")
elif operation == "-":
    print(f"{a} - {b} = {a - b}")
elif operation == "*":
    print(f"{a} * {b} = {a * b}")
elif operation == "/":
    print(f"{a} / {b} = {a / b}")
else:
    print("Wrong choise")

