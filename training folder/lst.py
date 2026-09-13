# number = [2, 5, 99, 42, 1, 0.4]
# number.insert(2, 1)
# print(sum(number))

# deleted = number.pop(0)
# print(f"list nubmer {number} | deleted {deleted}")

# numbers = [0, 1, 2, 3, 4, 5]

# for i in numbers:
#     print(i)

# language = ['Python', 'Java', 'C#']
# for index, element in enumerate(language):
#     if element == 'Python':
#         language.insert(1, "C++")
#     print(index, element)


# number = []
# for i in range(6):
#     number.append(i)
# print(number)


# nubmer = [i  for i in range(6) if i % 2 == 0]
# print(number)

number = [12, 5, 8, 99, 3, 8]
print(number[0], number[-1])
print(8 in number)
print(sum(number))
print(min(number))
print(max(number))

god = ['Zeus', 'Appolo', 'Ares']
god.append('Heroes')
god.insert(1, 'Hades')
god.remove('Appolo')
dele = god.pop(-1)
print(god, dele)


number = [4, 7, 10, 15, 18, 21, 24]
box = []
for index, num in enumerate(number):
    if num > 10:
        box.append(index)
print(box.__len__())


text = input()
srting = text.split(' ')
print(srting)
liist = '-'.join(srting)
print(liist)

a = [i**2 for i in range(1,11) if i % 3 != 0]
print(a)
    

    