# multi-way
weight = float(input())
if weight <= 60.0:
    print("light")
elif weight <= 64.0:
    print("halflight")
elif weight <= 69.0:
    print("halfmedium")
else:
    print("other")

age = int(input())
if age < 0 or age > 120:
    print("Error uncorrect age")
elif  0 <= age <= 2:
    print("littlechild")
elif  3 <= age <= 12:
    print("child")
elif  13 <= age <= 17:
    print("child")
elif 18 <= age <= 64:
    print("adult")
else:
    print("granny")
