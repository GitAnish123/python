# You can import as many classes as you need into a program file.

from car import Car, ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())



# You also can import an entire module using dot notation. Here is an example:

import car

my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())



# Here is how you import ALL classes from a module. 
# Import entire modules instead of this for clean imports and preventing name conflicts in your program file.

from car import *

print(my_mustang.get_descriptive_name())
print(my_leaf.get_descriptive_name())






# Now we can import from each module separately and create whatever kind of car we need.
# We are now about to import a module into a module!          (Use 'new_electric_car.py' and 'car.py' for reference.)
# Here is the example:

from car import Car
from new_electric_car import ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
# That is an example of how those kinds of advanced importing works!
# This could apply for real-world situations too!





# You also can use aliases to make calling/using them easier.
# As an example, consider a program where you want to make a bunch of electric cars. 
# It might get tedious to type (and read) ElectricCar over and over again. 
# You can give ElectricCar an alias in the import statement:

# Giving a class an alias.
from my_electric_car import ElectricCar as EC    # creating
my_leaf = EC('nissan', 'leaf', 2024)    # using


# You can give a module an alias as well!
import my_electric_car as ec
my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)

# These are some examples of how you can apply and inplument aliases in classes.
# You can use it for real-world situations as well!




# Finally, find your own workflow! Here is some advice to get started and think:
"""
As you can see, Python gives you many options for how to structure code in a large project. 
It's important to know all these possibilities. 
So then, you can determine the best ways to organize your projects as well as understand other people's projects.
When you're starting out, keep your code structure simple. 
Try doing everything in one file and moving your classes to separate modules once everything is working. 
If you like how modules and files interact, try storing your classes in modules when you start a project. 
Find an approach that lets you write code that works, and go from there.
"""
# Remember to read this carefully and also finding your own workflow is very important, so start simple!