def task_01():
    languages = ["Python", "Java", "C++", "JavaScript"]

    for index, lang in enumerate(languages):
        print(f"Index: {index}, Language: {lang}")
task_01()

def task_02():
    students = ["Alex", "Mary", "John"]
    for table_num, name in enumerate(students, start=1):
        print(f"Table №{table_num}: {name}")
task_02()

def task_03():
    names = ["Alice", "Bob", "Charlie", "David", "Eva"]

    for index, name in enumerate(names):
        if index % 2 == 0:
            print(f"Even index {index}: {name}")
task_03()