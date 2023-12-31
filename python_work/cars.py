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
        self.odometer_reading = 15     # This car has 15 miles on it

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2024)
my_new_car.update_odometer(12)   # It will say "You can't roll back an odometer because you can't go less!"
my_new_car.read_odometer()   # It will not change the value because of the warning message.
# That is an example of updating and adding logic by adding more methods!



# Additionally, you can increment a value using a method.
# This will increase the amount of the value. Select the value you want to increase it by and then it will add up.
# Here is a simple example:

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

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# The increment_odometer() method adds a specified mileage. After setting the initial odometer to 23,500, 
# 'increment_odometer(100)' includes the extra 100 miles driven before registration.
# That is an example of how incrementing works with a value being increased.
# We can modify the method to disallow negative increments, preventing the function from rolling back the odometer.

class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 15     # This car has 15 miles on it

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= self.odometer_reading:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(-100)  # It will result in an error
my_used_car.read_odometer()  # It will still be the same starting amount, 23500!
# That is an example of how to apply your skills and knowledge for commonn sense and logic for coding.
# That is an example to prevent rolling back odometers and incrementing a value using a method.







# ----------- PRACTICE -------------- #
""" Practice now begins """








# RESTAURANT (class 'Restaurant')




# Basic class of a restaurant with a default value and printing the value.
class Restaurant:
    """A simple representation of a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initillize attributes of a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Describe a restaurant"""
        print(f"The restaurant name is {self.restaurant_name} and the cuisine type is: {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Stimulate making a restaurant be opened."""
        print(f"{self.restaurant_name} is now currently open!")

restaurant = Restaurant('Dominoes', 'build-your-own and Specialty Pizzas')
print(f"This restaurant name is {restaurant.restaurant_name}. The cuisine type is: {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('Dominoes', 'build-your-own and Specialty Pizzas')
print(f"{restaurant.number_served} customers were served in {restaurant.restaurant_name}")   # Result:  0



# Lets change the value of the amount of served customers and printing value. (This is not the best way to modify values.)
class Restaurant:
    """A simple representation of a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initillize attributes of a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 2    # Changed value, not the best way/method to change the value.
    
    def describe_restaurant(self):
        """Describe a restaurant"""
        print(f"The restaurant name is {self.restaurant_name} and the cuisine type is: {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Stimulate making a restaurant be opened."""
        print(f"{self.restaurant_name} is now currently open!")

restaurant = Restaurant('Dominoes', 'build-your-own and Specialty Pizzas')
print(f"This restaurant name is {restaurant.restaurant_name}. The cuisine type is: {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('Dominoes', 'build-your-own and Specialty Pizzas')
print(f"{restaurant.number_served} customers were served in {restaurant.restaurant_name}")  # Result:  2



# Lets change the value DIRECTLY by modifying the amount of "served_customers" and printing value.
class Restaurant:
    """A simple representation of a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initillize attributes of a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Describe a restaurant"""
        print(f"The restaurant name is {self.restaurant_name} and the cuisine type is: {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Stimulate making a restaurant be opened."""
        print(f"{self.restaurant_name} is now currently open!")

restaurant = Restaurant('Dominoes', 'build-your-own and Specialty Pizzas')
print(f"This restaurant name is {restaurant.restaurant_name}. The cuisine type is: {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('Dominoes', 'build-your-own and Specialty Pizzas')
print(f"{restaurant.number_served} customers were served in {restaurant.restaurant_name}")  # Result:  0

restaurant = Restaurant('Dominoes', 'build-your-own and Specialty Pizzas')
restaurant.number_served = 2
print(f"{restaurant.number_served} customers were served in {restaurant.restaurant_name}")  # Result:  2



# Using a method to change the amount of served customers in a restaurant.
class Restaurant:
    """A simple representation of a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initillize attributes of a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Describe a restaurant"""
        print(f"The restaurant name is {self.restaurant_name} and the cuisine type is: {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Stimulate making a restaurant be opened."""
        print(f"{self.restaurant_name} is now currently open!")

    def set_number_served(self, customers_total):
        """Set the amount of customers that have been served, typically in a restaurant."""
        if customers_total >= self.number_served:
            self.number_served = customers_total
        else:
            print("You already had a greater amount of customers, you can't reduce the amount of customers served!")

restaurant = Restaurant('Dominoes', 'build-your-own and Specialty Pizzas')
print(f"This restaurant name is {restaurant.restaurant_name}. The cuisine type is: {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('Dominoes', 'build-your-own and Specialty Pizzas')
restaurant.set_number_served(25)
print(f"{restaurant.number_served} customers were served in {restaurant.restaurant_name}")  # Result:  25



# Using a method to increment the amount of served customers in a restaurant. (Adding/increasing more customers)
class Restaurant:
    """A simple representation of a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initillize attributes of a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 25
    
    def describe_restaurant(self):
        """Describe a restaurant"""
        print(f"The restaurant name is {self.restaurant_name} and the cuisine type is: {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Stimulate making a restaurant be opened."""
        print(f"{self.restaurant_name} is now currently open!")

    def set_number_served(self, customers_total):
        """Set the amount of customers that have been served, typically in a restaurant."""
        if customers_total >= self.number_served:
            self.number_served = customers_total
        else:
            print("You already had a greater amount of customers, you can't reduce the amount of customers served!")
    
    def increment_number_served(self, amount_increasing):
        """
        Increase the amount of customers that have been served, typically in a restaurant. 
        Increases the value then adds that value with the existing value to make the total value.
        """
        if amount_increasing >= self.number_served:
            self.number_served += amount_increasing
        else:
            print("You already had a greater amount of customers, you can't reduce the amount of customers served!")

restaurant = Restaurant('Dominoes', 'build-your-own and Specialty Pizzas')
print(f"This restaurant name is {restaurant.restaurant_name}. The cuisine type is: {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('Dominoes', 'build-your-own and Specialty Pizzas')
restaurant.increment_number_served(1024)
print(f"{restaurant.number_served} customers were served in {restaurant.restaurant_name}")  # Result:  1049. (25 + 1024)







# LOGIN ATTEMPTS (class 'User')




# Applying the same skills we did in the last example with the restaurant.
class User:
    """A simple representation to model a user"""
    def __init__(self, first_name, last_name, age, gender, height_in_inches, weight_in_pounds):
        """Initilize the attributes of the class user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.height_in_inches = height_in_inches
        self.weight_in_pounds = weight_in_pounds
        self.login_attempts = 0
    
    def describe_user(self):
        """Stimulate describing a user with some of the simple characteristics listed."""
        self.full_name = f"{self.first_name} {self.last_name}"
        print(f"The user name is {self.full_name}. (first: {self.first_name}) (last: {self.last_name})")
        print(f"{self.full_name}'s age is {self.age}, height in inches is {self.height_in_inches}, and weight in pounds is {self.weight_in_pounds}.")
        print(f"The gender of {self.first_name} is {self.gender}.")
    
    def greet_user(self):
        """Stimulate greeting a user by its full name."""
        self.full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello, {self.full_name}!")
    
    def increment_login_attempts(self):
        """
        Increase the amount of login attempts that have been there. 
        Increases the value then adds that value with the existing value to make the total value.
        """
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset the amount of login attempts to zero! Regarding all values, value is set to zero."""
        self.login_attempts = 0
    
    def show_amount_of_login_attempts(self):
        """Show the amount of login attempts to log in to a website or another source."""
        print(self.login_attempts)

user = User('Anish', 'Pasumarthi', 13, 'Male', 65, 98)

# Increasing the amount of login attempts from a user
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Showing the amount of login attempts
print("\nLogin attempts:")
user.show_amount_of_login_attempts()  # Result:  10

# Reset the amount of login attempts from a user
print("\nResetting login attempts")
user.reset_login_attempts()

# Showing the amount of login attempts
print("\nLogin attempts:")
user.show_amount_of_login_attempts()  # Result:  0








# --------- PRACTICE IS OVER ------------ #
""" PRACTICE IS CURRENTLY OVER!!! """










"""
When creating a specialized class that is based on another class, you can use inheritance. The new class, 
called the child class, inherits attributes and methods from the original class, known as the parent class. 
The child class can also define its own attributes and methods. To initialize attributes from the parent class, 
you often call the parent class's __init__() method in the child class. For instance, 
let's create an ElectricCar class based on the existing Car class, 
focusing only on the specific attributes and behaviors relevant to electric cars.
"""
# Here is the example:

class Car:
    """A simple attempt to represent a car."""

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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
    
class ElectricCar(Car):    # Using inheritance
    """A simple representation of a car, different aspects of a car, but specific to electric vehicles."""
    def __init__(self, make, model, year):         # Making its own "__init__()" method.
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)        # Accessing attributes to call methods from parent class
    
my_leaf = ElectricCar('nissan', 'leaf', 2024)      # Creating an instance
print(my_leaf.get_descriptive_name())        # Using any method from the parent class

# That is an example of how to use inhertitance.
# In this example, we are only testing if inhertitance works, not creating new attributes and methods.



# You can also define Attributes and Methods for the Child Class after you test inhertence from the child class!
# Here is an example of adding two attributes and methods:

class Car:
    """A simple attempt to represent a car."""

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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):
    """A simple representation of a car, different aspects of a car, but specific to electric vehicles."""
    def __init__(self, make, model, year, charging_time):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 40
        self.charging_time = charging_time
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def provide_charging_time(self):
        """Print a statement that provides the charging time, in minutes."""
        print(f"The charging time for the {self.make.title()} {self.model.title()} is {self.charging_time}.")

my_leaf = ElectricCar('nissan', 'leaf', 2024, 450)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.provide_charging_time()

# In "ElectricCar", add "self.battery_size" (initial: 40) ❶ and "describe_battery()" ❷ for electric car specifics.
# General car features belong in the "Car" class, ensuring broad functionality access.
# That is an example of how to add methods and attributes to a child class. These new ones will not appear in parent class.



# Additionally, you can also override/modify any method that doesn't fit what you're trying to model with the child class.
"""
You can override any method from the parent class that doesn't fit what you're trying to model with the child class. 
To do this, you define a method in the child class with the same name as the method you want to override in the parent class. 
Python will disregard the parent class method and only pay attention to the method you define in the child class. 
Say the class Car had a method called fill_gas_tank(). This method is meaningless for an all-electric vehicle, 
so you might want to override this method.
"""
# Here is the example:

class Car:
    """A simple attempt to represent a car."""

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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
    
    def fill_gas_tank(self):               # Lets assume this class has the method!
        """Stimulate filling a gas tank for a car."""          
        print("This car's fuel is filled with gas now!")
my_new_car = Car('audi', 'a4', 2024)
my_new_car.fill_gas_tank()   # This will fill the gas tank   

class ElectricCar(Car):
    """A simple representation of a car, different aspects of a car, but specific to electric vehicles."""
    def __init__(self, make, model, year, charging_time):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 40
        self.charging_time = charging_time
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def provide_charging_time(self):
        """Print a statement that provides the charging time, in minutes."""
        print(f"The charging time for the {self.make.title()} {self.model.title()} is {self.charging_time}.")
    
    def fill_gas_tank(self):   # We are overriding the method because electric cars don't have gas tanks so that won't make sense.
        """Electric cars don't have gas tanks."""
        print("This electric car has no gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024, 450)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.provide_charging_time()
my_leaf.fill_gas_tank()   # This will provide a message that you can't fill gas for an electric car!

# That is an example of how to override/modify methods that doesn't fit for a child class.
# You can apply these skills for other codes and programs/projects.



# Lets learn about composition!
# This is basically instances as attributes!
"""
In coding real-world situations, as your class grows with many details, you can simplify by using composition. 
For instance, if your ElectricCar class becomes too complex, 
create a separate class called Battery to handle battery-related details. 
Then, use a Battery instance as an attribute in the ElectricCar class.
"""
# Here is some BONUS and OPTIONAL rules/guidelines and tips!
"""
Composition is a design principle in object-oriented programming that involves creating instances of one class within 
another class. It emphasizes separation of concerns, ensuring that each class has a specific and independent responsibility. 
Unlike inheritance, 
composition does not involve an "is-a" relationship but instead encapsulates the functionality of one class within another, 
promoting modularity. This approach offers flexibility by allowing classes to be combined to form more complex structures, 
enhancing code reuse and maintainability. 
Instances of the composed class are typically created and initialized in the constructor of the containing class, 
and methods of the composed class can be delegated or called within the methods of the containing class. These rules 
contribute to a clear and meaningful relationship between classes and promote a structured and maintainable codebase.
"""
# Here is an example:

class Car:
    """A simple attempt to represent a car."""

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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):     # Creating an optional value. This value will be presented if no value provided.
        """Initialize the battery's attributes."""
        self.battery_size = battery_size   # Taking the value as a parameter.

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()     # Making the attribute as an instance

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()    # Accessing the method by first using the attribute.

# We introduce a class named Battery without inheritance, containing an optional battery_size parameter in its "init" method. 
# In the ElectricCar class, we add a self.battery attribute, 
# automatically creating a Battery instance with a default size of 40 for every ElectricCar instance.
# That is an example of how to use composition. Here are more examples of how to use it. 
# There are also so many ways & options for how to use composition. Here are some examples...


# Keeping it general with no default value(s) but defining the value in the "__init__()" line.
class Car:
    """A simple attempt to represent a car."""

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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size):    # No default value, and instead we are keeping it general.
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery(65)    # Providing a value

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()


# Same structure but creating an instance to store the attributes and calling it in the "__init__()" line.
class Car:
    """A simple attempt to represent a car."""

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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_battery = Battery(65)    # Creating an instance.

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = my_battery   # Using the instance here.

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()


# Here is another example for doing this. In the example, the "my_leaf" instance MUST provide the battery size as a parameter.
class Car:
    """A simple attempt to represent a car."""

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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size    # Keeping the parameter as the value

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, battery_size):   # Including the parameter in the "__init__()" line.
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery(battery_size)    # Changing the value

my_leaf = ElectricCar('nissan', 'leaf', 2024, 40)  # Including the battery size value as a parameter in the instance.
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

# These are some examples and explainations of what is composition and how to use it in many ways.



# This looks like a lot of extra work, 
# but now we can describe the battery in as much detail as we want without cluttering the ElectricCar class. 
# Let’s add another method to Battery that reports the range of the car based on the battery size:

class Car:
    """A simple attempt to represent a car."""

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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):      # New method provided
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):   
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()   

my_leaf = ElectricCar('nissan', 'leaf', 2024) 
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()    # Result:  This car can go about 150 miles on a full charge.

# The "get_range()" method in Battery analyzes and reports the range based on the car's battery attribute.
# That is an example of how to add more methods and be free for adding AS MANY methods and attributes you want.



# Lets learn some more tips.
# Here are some rules and tips of how to model real-world objects and understanding them followed by good practice skills.

"""
Modeling complex things like electric cars prompts interesting questions. 
Is the car's range a property of the battery or the car? 
If describing only one car, it's okay to keep the get_range() method in the Battery class. 
But for a whole lineup, it might be better in the ElectricCar class. 
This decision-making marks a shift to higher-level, logical thinking about code representation, 
where there's no strict right or wrong. Some approaches are more efficient, but finding the best takes practice. 
If your code works as intended, you're doing well. 
Don't be discouraged if you rewrite your classes several times; it's a common part of writing accurate, efficient code.
"""

# These are some tips and guidelines to model real-world objects and understand it as you dive deeper.
# Practice frequently/daily to write accurate and efficient code always for understanding, better results, and quickness.











# ----------- PRACTICE -------------- #
""" Practice now begins """










# Inherting a class along with adding a attribute and instance and finally creating an instance and calling it.
class Restaurant:   # Parent class
    """A simple representation of a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initillize attributes of a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 25
    
    def describe_restaurant(self):
        """Describe a restaurant"""
        print(f"The restaurant name is {self.restaurant_name} and the cuisine type is: {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Stimulate making a restaurant be opened."""
        print(f"{self.restaurant_name} is now currently open!")

    def set_number_served(self, customers_total):
        """Set the amount of customers that have been served, typically in a restaurant."""
        if customers_total >= self.number_served:
            self.number_served = customers_total
        else:
            print("You already had a greater amount of customers, you can't reduce the amount of customers served!")
    
    def increment_number_served(self, amount_increasing):
        """
        Increase the amount of customers that have been served, typically in a restaurant. 
        Increases the value then adds that value with the existing value to make the total value.
        """
        if amount_increasing >= self.number_served:
            self.number_served += amount_increasing
        else:
            print("You already had a greater amount of customers, you can't reduce the amount of customers served!")

class IceCreamStand(Restaurant):     # Child class
    """A simple representation of an ice-cream stand, but relating to a restaurant that shares the same information."""
    def __init__(self, restaurant_name, cuisine_type='ice cream'):   # Child class attributes
        """Create/review and access attributes for a child class."""
        super().__init__(restaurant_name, cuisine_type)    # Telling to refer the superclass (parent class)
        self.flavors = []   # Empty list, we can modify it when we create an instance.
    
    def display_ice_cream_flavors(self):   # New method and using the new attribute
        """Display all the ice cream flavors avaliable in the ice-cream stand."""
        print("\nHere are all the ice-cream flavors available:")
        for flavor in self.flavors:   # Looping through the list
            print(f"-- {flavor}")

ice_cream = IceCreamStand('Marble Slab Creamery')
ice_cream.flavors = ['strawberry', 'mint chocolate ship', 'vanilla', 'chocolate', 'butterscotch', 'cotton candy', "cookies 'n cream"]

ice_cream.describe_restaurant()
ice_cream.display_ice_cream_flavors()



# Another example of the SAME concept by applying users and admins.
class User:
    """A simple representation to model a user"""
    def __init__(self, first_name, last_name, age, gender, height_in_inches, weight_in_pounds):
        """Initilize the attributes of the class user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.height_in_inches = height_in_inches
        self.weight_in_pounds = weight_in_pounds
        self.login_attempts = 0
    
    def describe_user(self):
        """Stimulate describing a user with some of the simple characteristics listed."""
        self.full_name = f"{self.first_name} {self.last_name}"
        print(f"The user name is {self.full_name}. (first: {self.first_name}) (last: {self.last_name})")
        print(f"{self.full_name}'s age is {self.age}, height in inches is {self.height_in_inches}, and weight in pounds is {self.weight_in_pounds}.")
        print(f"The gender of {self.first_name} is {self.gender}.")
    
    def greet_user(self):
        """Stimulate greeting a user by its full name."""
        self.full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello, {self.full_name}!")
    
    def increment_login_attempts(self):
        """
        Increase the amount of login attempts that have been there. 
        Increases the value then adds that value with the existing value to make the total value.
        """
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset the amount of login attempts to zero! Regarding all values, value is set to zero."""
        self.login_attempts = 0
    
    def show_amount_of_login_attempts(self):
        """Show the amount of login attempts to log in to a website or another source."""
        print(self.login_attempts)

class Admin(User):
    """A simple representation of a User, but relating to a Admin for specific information for that type of person."""
    def __init__(self, first_name, last_name, age, gender, height_in_inches, weight_in_pounds):
        """Initialize attributes of an Admin child class that is specific to a User class."""
        super().__init__(first_name, last_name, age, gender, height_in_inches, weight_in_pounds)
        self.basic_privileges = ["can add post", "can delete post", "can ban user", "can add user", "can see user's info/records", "can track user", "can fire user", "can direct user", "can call user", "can schedule almost anything"]
    
    def show_privileges(self):
        """Show the lists the administrator's set of privileges."""
        print("\nHere are SOME of the BASIC privileges an admin can do:")
        for the_privilege in self.basic_privileges:
            print(f"-- {the_privilege}")

admin = Admin('Justin', 'Champ', 41, 'Male', 69, 153)   # Creating new instance
admin.show_privileges()   # Calling method



# Creating an instance as an attribute with a new class that stores more specific information related to a child class.
class User:   
    """A simple representation to model a user"""     # The original parent class
    def __init__(self, first_name, last_name, age, gender, height_in_inches, weight_in_pounds):
        """Initilize the attributes of the class user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.height_in_inches = height_in_inches
        self.weight_in_pounds = weight_in_pounds
        self.login_attempts = 0
    
    def describe_user(self):
        """Stimulate describing a user with some of the simple characteristics listed."""
        self.full_name = f"{self.first_name} {self.last_name}"
        print(f"The user name is {self.full_name}. (first: {self.first_name}) (last: {self.last_name})")
        print(f"{self.full_name}'s age is {self.age}, height in inches is {self.height_in_inches}, and weight in pounds is {self.weight_in_pounds}.")
        print(f"The gender of {self.first_name} is {self.gender}.")
    
    def greet_user(self):
        """Stimulate greeting a user by its full name."""
        self.full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello, {self.full_name}!")
    
    def increment_login_attempts(self):
        """
        Increase the amount of login attempts that have been there. 
        Increases the value then adds that value with the existing value to make the total value.
        """
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset the amount of login attempts to zero! Regarding all values, value is set to zero."""
        self.login_attempts = 0
    
    def show_amount_of_login_attempts(self):
        """Show the amount of login attempts to log in to a website or another source."""
        print(self.login_attempts)

class Privileges:   # New class
    """A simple attempt to model privileges for an admin to do when nessesary or normally."""
    def __init__(self, basic_privileges):
        """Initialize attributes for a class."""
        self.basic_privileges = basic_privileges 
    
    def show_privileges(self):    # Using the method in this area
        """Show the lists the administrator's set of privileges."""
        print("\nHere are SOME of the BASIC privileges an admin can do:")
        for the_privilege in self.basic_privileges:
            print(f"-- {the_privilege}")   

# Create an instance
admin_privilege = Privileges(["can add post", "can delete post", "can ban user", "can add user", "can see user's info/records", "can track user", "can fire user", "can direct user", "can call user", "can schedule almost anything"])

class Admin(User):
    """A simple representation of a User, but relating to a Admin for specific information for that type of person."""
    def __init__(self, first_name, last_name, age, gender, height_in_inches, weight_in_pounds):
        """Initialize attributes of an Admin child class that is specific to a User class."""
        super().__init__(first_name, last_name, age, gender, height_in_inches, weight_in_pounds)
        self.privilege = admin_privilege   # Using the instance as an attribute

admin = Admin('Justin', 'Champ', 41, 'Male', 69, 153)   # Creating new instance
admin.privilege.show_privileges()   # Accessing and calling the method



# Modeling real-world objects by creating a new method and keeping it in the right area with the right job.
class Car:
    """A simple attempt to represent a car."""

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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):     
        """Initialize the battery's attributes."""
        self.battery_size = battery_size  

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):      
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):   # Creating a new method at the right spot.
        """Upgrade a battery to 65 kWh no matter any size it is."""
        if self.battery_size:  # If there is a battery...
            if self.battery_size != 65:
                self.battery_size = 65
                print("Processing upgrade...\tGetting it ready...\nBattery successfully upgraded!")
                print("This car has now at 65 kWh battery!")
            else:
                print("Battery is already upgraded to max size!")
        else:    # If there is no battery...
            print("No BATTERY PROVIDED!\nPlease provide a battery for upgrading.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()  

my_leaf = ElectricCar('nissan', 'leaf', 2024)   # Creating an instance

my_leaf.battery.battery_size = 40    # Setting the battery size to 40 kWh
my_leaf.battery.describe_battery()   # Describing the battery
my_leaf.battery.get_range()   # Result:  This car can go about 150 miles on a full charge.

my_leaf.battery.upgrade_battery()   # Using the method to upgrade the battery to 65 kWh, the max size!
my_leaf.battery.describe_battery()  # Describing the battery again, this will show an upgraded result.
my_leaf.battery.get_range()   # Result:  This car can go about 225 miles on a full charge.

# These examples above are ways of how inhertence works & ways we can use these classes for deeper knowledge & understanding.











# --------- PRACTICE IS OVER ------------ #
""" PRACTICE IS CURRENTLY OVER!!! """








# Lessons are currently on the other "car" files!
# Refer to them if you want to learn to import classes, finding workflows, using aliases, and more!











                ########### LESSONS CURRENTLY FINISHED BY DEFAULT ############
"""Lessons are currently finished by default, program ends!"""