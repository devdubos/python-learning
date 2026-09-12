student = {
    "name": "Alex",
    "age": 20,
    "grades": [85, 90, 78, 92]
}
print(student["name"])
average_grade = sum(student["grades"]) / len(student["grades"])
print(average_grade)
student["status"] = "active"
print(student)

text = "programming"
letter_count = {}

for letter in text:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count)