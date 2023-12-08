cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list:")
print(cars)
print("\nHere is reverse order of the sorted list:")
print(sorted(cars, reverse=True))
print("\nHere is the original list once again:")
print(cars)
cars = ['bmw','audi','toyota','subaru']
print(len(cars))

# You can also loop
cars = ['bmw','audi','toyota','subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# This is how you do an "if" statement
# This is a simple example.

car = 'bmw'
print(car == 'bmw')
car = 'audi'
print(car == 'bmw')

car = 'Audi'
print(car == 'audi')
car = 'Audi'
print(car.lower() == 'audi')
car = 'Audi'
print(car.lower() == 'audi')

# Now lets check if our original variable got affected when we used the "lower()" method,
print(car)
# The result is "Audi" so the value as not been affected by the method.
# One more example...

car = 'Audi'
print(car != 'Audi')
print(car != 'bmw')
# This sign indicates "not equal to operator"





# Lets create the car class with attributes & methods! To begin this journey of different learning and aspects of classes...
# Lets create the basic car class with just one method!
class Car:
    """A simple attempt to represent a car."""
     
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
# That is a simple representation of a car. Get ready for more updates and more learning.



# Lets create a default value for a class. 
# When an instance is created, attributes can be defined without being passed in as parameters.
# These attributes can be defined in the "__init__()"" method, where they are assigned a default value.
# Let’s add an attribute called odometer_reading that always starts with a value of 0. 
# We’ll also add a method read_odometer() that helps us read each car’s odometer. Here is the example:

class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# That is an example of how to create a default value for a class.



# You also can modify a method. There are three ways...
# direct instance change, set value through a method, or increment the value.
# Here is an example of directly changing the value by instance.

class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# That is a simple example of how you do it.



# Lets learn how to set a value through a method. Here is a simple example:
class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

# We can extend the method update_odometer() to do additional work every time the odometer reading is modified. 
# Let’s add a little logic to make sure no one tries to roll back the odometer reading:

class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if self.odometer_reading >= mileage:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
# That is an example of updating and adding logic by adding more methods!