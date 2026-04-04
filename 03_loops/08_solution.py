# Problem: Check if a number is prime.
# Prime numbers are whole numbers greater than 1 that have exactly two factors: 1 and themselves

number = 29
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(number ,"is a prime number", is_prime)