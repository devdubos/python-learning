result = 0
for i in range (5):
    num = int(input())
    if num < 0:
        print("no sorry")
        break
    result += num
print('summ all number:', result)
