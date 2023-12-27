"""
The Python standard library is a set of modules included with every Python installation. 
Now that you have a basic understanding of how functions and classes work, 
you can start to use modules like these that other programmers have written. 
You can use any function or class in the standard library by including a simple import statement at the top of your file. 
Let's look at one module, random, which can be useful in modeling many real-world situations.
One interesting function from the random module is randint(). 
This function takes two integer arguments and returns a randomly selected integer between (and including) those numbers.
"""
# Here’s how to generate a random number between 1 and 6:

from random import randint   # Importing the function from the module
print(randint(1,6))          # Generates a random integer between 1-6



# Another useful function is "choice()". This function takes in a list or tuple and returns a randomly chosen element:
from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up.title())



"""
The random module shouldn't be used when building security-related applications, 
but it works well for many fun and interesting projects.
"""
# These are some examples that are inside the Python Standard Library. There are SO MANY more modules/functions to explore.

"""
NOTE:
You can also download modules from external sources. 
You'll see a number of these examples, where we'll need external modules to complete each project.
"""











# ----------- PRACTICE -------------- #
""" Practice now begins """












# Using the "random" module from the standard library to create a dice program!
from random import randint

class Die:
    """A simple representation of a die with any amount of sides that could be used in probability."""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Stimulate rolling a die and finding the resulted number of the roll."""
        rolled_result = randint(1, self.sides)
        return rolled_result
    
# Creating an instance and rolling a 6-sided die and a 10-sided die.
my_six_sided_die = Die()
print(my_six_sided_die.roll_die())

my_ten_sided_die = Die(10)
print(my_ten_sided_die.roll_die())





# Using the "random" module to make a lottery that tells the final winning ticket is!
from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = []
print("Lets see what the winning ticket is...")

# Use a while loop so we don't get repeated winning letters and numbers
while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)
    
    # Only add the pulled item to the winning ticket if it hasn't already been pulled.
    if pulled_item not in winning_ticket:
        print(f"  We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)

print(f"\nThe final winning ticket is: {winning_ticket}")





# Using lottery analysis to make the program more interesting!
from random import choice

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    # We don't want to repeat winning numbers or letters, so we'll use a
    #   while loop.
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the winning ticket if it hasn't
        #   already been pulled.
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    # Check all elements in the played ticket. If any are not in the 
    #   winning ticket, return False.
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket!
    return True

def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    # We don't want to repeat numbers or letters, so we'll use a while loop.
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the ticket if it hasn't already
        #   been pulled.
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# Let's set a max number of tries, in case this takes forever!
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")














# --------- PRACTICE IS OVER ------------ #
""" PRACTICE IS CURRENTLY OVER!!! """