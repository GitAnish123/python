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