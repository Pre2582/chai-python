# Problem: Create a recursive function to calculate the factorial of a number.

# def addNum(a, b):
#     addNum(2, 3)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))