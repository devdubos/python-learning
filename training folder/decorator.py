import time
from functools import wraps


def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} sec.")
        return result
    return wrapper


@timer_decorator
def process_data(items: list[int]) -> list[int]:
    time.sleep(0.3)
    return [x ** 2 for x in items if x % 2 == 0]


if __name__ == "__main__":
    numbers = list(range(1, 20))
    squared_evens = process_data(numbers)
    print("Result:", squared_evens)
