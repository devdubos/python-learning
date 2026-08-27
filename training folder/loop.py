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


secret_number = 7
user_guess = 0

# Simulating user inputs: 3, 5, 7
guesses = [3, 5, 7]
index = 0

while user_guess != secret_number:
    user_guess = guesses[index]
    print(f"User guessed: {user_guess}")
    index += 1

print("Correct guess!")