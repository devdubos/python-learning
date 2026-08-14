nums = [5, 2, 8, 1, 9, 3]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))

nums = [12, 45, 7, 23, 56, 3]
difference = max(nums) - min(nums)
average = sum(nums) / len(nums)
print(difference)
print(average)

fruits = ['яблоко', 'банан', 'апельсин', 'груша', 'киви']
sorted_fruits = sorted(fruits)
print(sorted_fruits)
print(fruits)

nums = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_desc = sorted(nums, reverse=True)
print(sorted_desc)