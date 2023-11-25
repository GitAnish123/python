# Ways to import modules and functions!!!
# Different teqniques and ways are below...



# Importing the "pizza" module and using the module for the functions to be used.
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# We can import specific functions!
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Using the keyword, "as" to give a function an alias.
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# You can also directly give a module an alias. This is an effietient way to call functions much quicker.
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# You can import all the functions from a module using an asterisk. This is not recommonded for larger modules.
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# These are some ways and teqniques for importing functions and modules.
# Make sure follow tips and guidelines in notes and websites for styling functions!