names = ["Alice", "Bob", "Charlie"]

names_iterator = iter(names)

print(next(names_iterator))
print(next(names_iterator))
print(next(names_iterator))

def custom_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            print(f"Processing item: {item}")
        except StopIteration:
            print("Iteration finished cleanly")
            break

data = [10, 20, 30, 40]
custom_for_loop(data)

def task_eat():
    menu = ["Pizza", "Sushi", "Borsch"]

    menu_iterator = iter(menu)

    print(next(menu_iterator))
    print(next(menu_iterator))
    print(next(menu_iterator))

    try:
        print(next(menu_iterator))
    except StopIteration:
        print("No more items!")
task_eat()