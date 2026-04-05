# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
# Create an instance of the Car class
my_car = Car("Toyota", "Corolla")
# Print the attributes of the car
# print(f"Brand: {my_car.brand}, Model: {my_car.model}")

my_new_car = Car("Honda", "Civic")
# print(f"Brand: {my_new_car.brand}, Model: {my_new_car.model}")  


# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
# Create an instance of the Car class
my_car = Car("Toyota", "Corolla")
# print(my_car.full_name())
my_new_car = Car("Honda", "Civic")
# print(my_new_car.full_name())   


# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
# Create an instance of the ElectricCar class
my_electric_car = ElectricCar("Tesla", "Model 3", "75 kWh")
# print(my_electric_car.full_name())
# print(f"Battery Size: {my_electric_car.battery_size}")
    


# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand
    
# Create an instance of the Car class
my_car = Car("Toyota", "Corolla")   
# print(f"Brand: {my_car.get_brand()}, Model: {my_car.model}")

# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand

    def fuel_type(self):
        return "Gasoline"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electricity"
# Create instances of Car and ElectricCar
my_car = Car("Toyota", "Corolla")
my_electric_car = ElectricCar("Tesla", "Model 3", "75 kWh")

# print(my_car.fuel_type())
# print(my_electric_car.fuel_type())



# Problem: Add a class variable to Car that keeps track of the number of cars created.
class Car:
    car_count = 0  # Class variable to keep track of the number of cars created

    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.model = model
        # Car.car_count += 1  # Increment the car count when a new car is created
        self.__class__.car_count += 1  # Increment the car count when a new car is created

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand

    def fuel_type(self):
        return "Gasoline"


# print(f"Total cars created: {Car.car_count}")
my_car1 = Car("Toyota", "Corolla")
my_car2 = Car("Honda", "Civic")
# print(f"Total cars created: {Car.car_count}")
# # my_electric_car = ElectricCar("Tesla", "Model 3", "75 kWh")
# print(f"Total cars created: {Car.car_count}")


# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    car_count = 0  # Class variable to keep track of the number of cars created

    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.model = model
        self.__class__.car_count += 1  # Increment the car count when a new car is created

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand

    def fuel_type(self):
        return "Gasoline"

    @staticmethod  #use beacuse we want to call this method without creating an instance of the class
    def general_description():
        return "A car is a road vehicle, typically with four wheels, powered by an internal combustion engine or electric motor."   

# print(Car.general_description())


# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    car_count = 0  # Class variable to keep track of the number of cars created

    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.__model = model  # Private attribute
        self.__class__.car_count += 1  # Increment the car count when a new car is created

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def get_brand(self):
        return self.__brand

    @property   #use beacuse we want to access the model as an attribute, not a method
    def model(self):
        return self.__model
    def fuel_type(self):
        return "Gasoline"
my_car = Car("Toyota", "Corolla")
# print(my_car.model)  # Accessing the model using the property


# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

class Car:
    car_count = 0  # Class variable to keep track of the number of cars created

    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.__model = model  # Private attribute
        self.__class__.car_count += 1  # Increment the car count when a new car is created

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def get_brand(self):
        return self.__brand

    @property   #use beacuse we want to access the model as an attribute, not a method
    def model(self):
        return self.__model
    def fuel_type(self):
        return "Gasoline"
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electricity"
my_tesla = ElectricCar("Tesla", "Model 3", "75 kWh")
# print(isinstance(my_tesla, Car))  # True, because ElectricCar is a subclass of Car
# print(isinstance(my_tesla, ElectricCar))  # True, because my_tesla is an instance of ElectricCar



# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Car:
    car_count = 0  # Class variable to keep track of the number of cars created

    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.__model = model  # Private attribute
        self.__class__.car_count += 1  # Increment the car count when a new car is created

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def get_brand(self):
        return self.__brand

    @property   #use beacuse we want to access the model as an attribute, not a method
    def model(self):
        return self.__model
    def fuel_type(self):
        return "Gasoline"
class Battery:
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def battery_info(self):
        return f"Battery size: {self.battery_size}"
class Engine:
    def engine_info(self):
        return "This is an engine."
class ElectricCar(Car, Battery, Engine):
    def __init__(self, brand, model, battery_size):
        Car.__init__(self, brand, model)  # Initialize Car part
        Battery.__init__(self, battery_size)  # Initialize Battery part

    def fuel_type(self):
        return "Electricity"    

my_tesla = ElectricCar("Tesla", "Model 3", "75 kWh")
print(my_tesla.full_name())  # From Car class
print(my_tesla.battery_info())  # From Battery class
print(my_tesla.engine_info())  # From Engine class

