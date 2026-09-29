# phone_number = " +375295774545"
# len(phone_number)
# if phone_number.strip().startswith("+3"):
#     print("Belarus number")
# else:
#     print("Unknow number")

# phone_number = phone_number.replace("+3","+7")
# print(phone_number)


# full_name = "   pYthOOn tHE GReat Lang  "
# full_name = full_name.strip().lower().capitalize()
# print(full_name)
# print(f"{full_name[0]}.{full_name[-1]}")

string = 'Im the future python dev'
my_list = string.split()
print(my_list)
sting = ' '.join(my_list)
# print(string)

def double_char(s):
    result = ""
    for i in s:
        result += i*2
    return result 

print(double_char('String'))

def sum_mix(arr):
    box = 0
    for i in arr:
        if i == str:
            i == int
    for i in arr:
        box += i
    return box


def smart_log_formatter(logs):
    if not logs:
        return []
    result = []
    count = 1
    previos = logs[0]
    for i in logs[1:]:
        if i == previos:
            count +=1 
        else:
            if count > 1:
                result.append(f"{previos} (x{count})")       
            else:
                result.append(previos)
            count = 1
            previos = i
    if count > 1:
        result.append(f"{previos} (x{count})")      
    else:
        result.append(previos)
    return result

print(smart_log_formatter([
                    "ERROR Disk failure",
                    "ERROR Disk failure",
                    "ERROR Disk failure",
                    "INFO User login",
                    "INFO User login"
                ]))


def two_oldest_ages(ages):
    ages_copy = list(ages)
    result = []
    a = max(ages_copy)
    result.append(a)
    ages_copy.remove(a)
    b = max(ages_copy)
    result.insert(0,b)
    return result
        
            
def remov_nb(n):
    total_sum = n * (n + 1) // 2
    result = []
    for a in range(1, n + 1):
        b = (total_sum - a) / (a + 1)
        if b.is_integer() and 1 <= b <= n:
            result.append((a, int(b)))
    return result

def high_and_low(numbers):
    nums = [int(x) for x in numbers.split()]
    return f"{max(nums)} {min(nums)}"