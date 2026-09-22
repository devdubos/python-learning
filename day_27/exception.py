
# try:
#     number = int(input("Write number: "))
#     print(10 / number)
# except ZeroDivisionError:
#     print('Bro dont input 0')
# except ValueError:
#     print('Bro dont input str')


# ZeroDivisionError:
# ValueError:

# try:
#     number = int(input("Write number: "))
#     print(10 / number)
# except Exception as error:
#     print(f"Something wrong:{error}")
# else:
#     print("Error dont exist")
# finally:
#     print("Code end. This text always shows couse we write 'finaly' ")

# age = int(input())
# if age <= 0:
#     raise ValueError("We have bad news")
try:
    user = {
        'name': 'Sergey',
        'age': '24'
    }
    print(user['email'])
except KeyError:
    print('Key email dont exist')



