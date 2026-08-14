list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

zeros = [0] * 5
repeated = [1, 2] * 4
print(zeros)
print(repeated)

animals = ['кот', 'собака', 'слон', 'тигр']
print('слон' in animals)
print('лев' in animals)

nums = [10, 20, 30, 40, 50, 60]
del nums[2]
print(nums)
del nums[-1]
print(nums)

nums = [5, 10, 15, 20, 25]
del nums[2]
print(10 in nums)
new_list = nums * 2
print(new_list)