# Lets learn about classes
# Here is some information about classes!
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