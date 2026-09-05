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