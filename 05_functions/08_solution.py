# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

# def print_kwargs(name, power):
#     print("Name: ", name, "Power: ", power)

# print_kwargs(name = "shaktiman", power = "lazer")    
# print_kwargs(power = "lazer", name = "shaktiman", enemy = "Dr. Jackaal")   

def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name = "shaktiman", power = "lazer")    
print_kwargs(power = "lazer", name = "shaktiman", enemy = "Dr. Jackaal")    

