# Lets learn about classes
# Here is some information about classes! Learn more in the notes if you need help!
"""
Object-oriented programming (OOP) is a potent software development method. It creates classes for real-world entities and 
generates objects based on them, defining general behavior for object categories. Instantiation, creating objects from a 
class, imbues them with general behavior and allows customization for unique traits, effectively modeling real-world 
scenarios. Learning OOP involves writing classes, creating instances, specifying stored information, and defining actions. 
Extending class functionality shares traits, boosting efficiency with less code. Organizing classes into modules and 
importing others' classes enhances code structure. Understanding OOP aids programmers in comprehending code at both 
line-by-line and conceptual levels, fostering logical thinking for effective problem-solving. Collaboration benefits of 
shared OOP logic include mutual understanding among programmers, facilitating teamwork on complex challenges. Consistent 
logic application results in comprehensible programs, increasing overall productivity.
"""

# Here is an example of a simple class model by a Dog class:
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
     
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
"""
First we create a class named Dog using capitalized letters. No parentheses are used in the class definition, 
signaling its creation from scratch. A docstring is included to describe the class briefly. There is a lot of information
that will be covered throughout this unit!
"""


"""
In Python, a method is a function inside a class. The init() method is special; it runs automatically when we create a 
new instance of a class, like Dog. Use double underscores on each side (e.g., init()). The init() method in the Dog class has 
three parameters: self, name, and age. "Self" refers to the instance itself. When creating a Dog instance, 
Python automatically passes self, so we only need to provide values for name and age. Variables with the "self" prefix, like 
self.name and self.age, are attributes accessible to every method in the class. These attributes are assigned values when 
creating an instance. The Dog class also has two other methods: sit() and roll_over(). They have only one parameter, self, 
and can be extended for more complex actions in a realistic scenario, like animating a dog in a game or controlling a 
robotic dog's movements.
"""


# You can create an instance from a class. Here is an example from the dog class!
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
     
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)  # Creating a instance for the class

print(f"My dog's name is {my_dog.name}.")  # Using the attribute, "name"
print(f"My dog is {my_dog.age} years old.")  # Using the attribute, "age"
# That is an example of how to create instances/objects by accessing the attributes we have to enter.


# What we are doing above is accessing attributes. Here is the line of the code we are talking about:
print(my_dog.name)
# Dot notation is crucial as it helps find attribute values. Python will just look for the attrubite name in this example.



# As well as accessing attributes, you can call methods in a class that we defined. Here is an example:
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()
# This syntax is useful when names are descriptive as it aids better understanding to the code. That is a simple example.



# Additionally, you can create as many instances as you want. Here is an example...
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
     
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()
# In Python, even if names and ages are the same, each new dog instance is separate. 
# You can create many instances from one class, but each needs a unique name or position in a list or dictionary.






# ----------- PRACTICE -------------- #
""" Practice now begins """





# Create a class restaurant with two methods and attributes.
class Restaurant:
    """A simple representation of a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initillize attributes of a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
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



# Creating more instances
class Restaurant:
    """A simple representation of a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initillize attributes of a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        """Describe a restaurant"""
        print(f"The restaurant name is {self.restaurant_name} and the cuisine type is: {self.cuisine_type}.")
    def open_restaurant(self):
        """Stimulate making a restaurant be opened."""
        print(f"{self.restaurant_name} is now currently open!")

restaurant = Restaurant('Dominoes', 'America')
print(f"This restaurant name is {restaurant.restaurant_name}. The cuisine type is: {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('Dominoes', 'pizza')
restaurant.describe_restaurant()

restaurant2 = Restaurant('Taco Bell', 'tacos')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Chick-Fil-A', 'sandwiches')
restaurant3.describe_restaurant()


