# student = {
#     "name": "Alex",
#     "age": 20,
#     "grades": [85, 90, 78, 92]
# }
# print(student["name"])
# average_grade = sum(student["grades"]) / len(student["grades"])
# print(average_grade)
# student["status"] = "active"
# print(student)

# text = "programming"
# letter_count = {}

# for letter in text:
#     if letter in letter_count:
#         letter_count[letter] += 1
#     else:
#         letter_count[letter] = 1

# print(letter_count)

# author = {
#     "name": "Sergey",
#     "age": 18,
#     "surname": "dub",
# }

# print(author.get("surname", "Duboss"))

# author["age"] = 19
# author["is_mentor"] = True
# author.pop("name")
# print(author)


# author = {
#     "name": "Sergey",
#     "age": 18,
#     "is_dev": True,
# }

# for pair in author.keys():
#     print(pair)

# for pair in author.values():
#     print(pair)

# for pair in author.items():
#     print(pair)

# print(*author.items(),sep="\n")


user = {
    "name": "Sergey",
    "surname": "Dubos",
    "city": "Minsk"
}
print(user['name'])
print(user.get('surname'))

user["city"] = "Edinburg"
user["learning_python"] = True
user.pop('city')
for keys, values in user.items():
    print(keys,"-", values)



