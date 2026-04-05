# Problem: Write a decorator that measures the time a function takes to execute.
# Solution:
# import time     use this for time calculation

import time
def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

# @timeit
# def example_function(n):
#     total = 0
#     for i in range(n):
#         total += i
#     return total

@timeit
def example_function(n):
    time.sleep(n)  # Simulate a time-consuming task


# example_function(1000000)
example_function(2)  # This will sleep for 2 seconds and print the execution time
