age = 20

access = "Access granted" if age >= 18 else "Access denied"
print(access)

num = 7

result = "Even" if num % 2 == 0 else "Odd"
print(result)

x = -5

sign = "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")
print(sign)


score = 4

feedback = "Excellent" if score == 5 else ("Good" if score == 4 else "Try harder")
print(feedback)
a = 12
b = 25
c = 7
max_num = (a if a > c else c) if a > b else (b if b > c else c)
print(max_num)
