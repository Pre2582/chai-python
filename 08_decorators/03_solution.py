# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
def cache(func):
    cache_dict = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_dict:
            print(f"Using cached value for {func.__name__} with arguments: {args} and keyword arguments: {kwargs}")
            return cache_dict[key]
        else:
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result
    return wrapper

@cache
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(example_function(1000000))
print(example_function(1000000))



import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(4, 3))