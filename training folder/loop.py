count = 0
while count < 5:
    print("hello")
    count += 1
    
text = "hello world"
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

n = 5

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


    num = 12345
digit_sum = 0

while num > 0:
    digit_sum += num % 10
    num = num // 10

print("Sum of digits:", digit_sum)