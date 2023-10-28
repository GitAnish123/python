# You can use the "remove()" method to remove any specific instances in a list.
# Lets do the value "cat" for an example,
""" for example: """

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


# So we have our old list and our new list.
# You can apply this situation to harder concepts.






##  PRACTICE STARTS NOW ##
""" Practice is currently starting now"""




# using "while" loops with lists
sandwich_orders = ['tuna sandwich', 'potato sandwich', 'cheese sandwich', 'peanut-butter sandwich', 'chicken sandwich']
finished_sandwiches = []
while sandwich_orders:
    sandwiches = sandwich_orders.pop()

    finished_sandwiches.append(sandwiches)
    print(f"\nI am working on your {sandwiches}")

print("Here are the sandwiches completed: ")
for sandwich in finished_sandwiches:
    print(sandwich)



# using "while" loops to remove certain kinds of elements
sandwich_orders = ['tuna sandwich', 'pastrami', 'potato sandwich', 'cheese sandwich', 'pastrami', 'peanut-butter sandwich', 'chicken sandwich', 'pastrami']
finished_sandwiches = []

print("We're extremely sorry, we ran out of pastrami sandwiches!")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwiches = sandwich_orders.pop()

    finished_sandwiches.append(sandwiches)
    print(f"\nI am working on your {sandwiches}")

print("Here are the sandwiches completed: ")
for sandwich in finished_sandwiches:
    print(sandwich)



# using "while" loops with dictionaries
vacation = {}
vacation_active = True

while vacation_active:
    name = input("What is your name?  ")
    poll = input("If you would visit anywhere in the world, where would you go?  ")
    vacation[name] = poll

    respond_again = input("Is there anybody else to respond (yes, no)?  ")
    if respond_again != "yes":
        vacation_active = False

print(" --- Poll Results --- ")
for name, poll in vacation.items():
    print(f"{name.title()} will want to visit {poll.title()}")





# If you want to add more user input about asking more info...
vacation = {}
vacation_active = True

while vacation_active:
    name = input("What is your name?  ")
    age = input("What is your age? ")
    age = int(age)
    location = input("Where do you currently live?  ")
    poll = input("If you would visit anywhere in the world, where would you go?  ")
    vacation[name] = {
        "age": age,
        "location": location,
        "poll": poll,
    }

    respond_again = input("Is there anybody else to respond (yes, no)?  ")
    if respond_again != "yes":
        vacation_active = False

print(" --- Poll Results --- ")
for name, info in vacation.items():
    print(f"{name.title()} will want to visit {info['poll'].title()}")
    print(f"{name.title()} is {info['age']} years old and lives in {info['location'].title()}")





# Lets do the code but lets use the break statement. (Lets do the unique and long example)
vacation = {}

while True:
    name = input("What is your name?  ")
    age = input("What is your age? ")
    age = int(age)
    location = input("Where do you currently live?  ")
    poll = input("If you would visit anywhere in the world, where would you go?  ")
    vacation[name] = {
        "age": age,
        "location": location,
        "poll": poll,
    }

    respond_again = input("Is there anybody else to respond (yes, no)?  ")
    if respond_again != "yes":
        break

print(" --- Poll Results --- ")
for name, info in vacation.items():
    print(f"{name.title()} will want to visit {info['poll'].title()}")
    print(f"{name.title()} is {info['age']} years old and lives in {info['location'].title()}")





###### END OF PRACTICE #######
""" This is the end of practice"""





# We can use multiple arguments and parameters to do more effietient jobs in functions!
# For example,


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
# This will print the information you need!




# You can also call multiple functions calls!
# For example...

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')




# Make sure to order your arguments correctly, or otherwise you could get unexpected results like this:
# For example,

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')
# In summary, make sure to order arguments in a function appropriatly!




# To not worry about the order of the arguments, use keyword arguments methods!
# For example, watch the example and learn.  (See notes if you need help)

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

# It doesn't matter which order you do it. These following codes are equivalent and will give you same result.
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# That is two examples of keyword arguments!




# You can have default values to simplify the amount of work you do!
# For example,

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
# You also can instead use postitional arguments and do this:
describe_pet('willie')  # Same output

# To describe another kind of animal, (If you don't want to use dog) use the parameter to do it.
describe_pet(pet_name='harry', animal_type='hamster')
# Make sure all default values defined should be defiend at the END to avoid postitional errors!
# The function now requires ONE postional argument, "pet_name".





# The function calls have multiple equalivalent ways to be called.
# Consider the following definition for "describe_pet()"" with one default value provided:
"""   def describe_pet(pet_name, animal_type='dog'):   """
# All these calls would work and give the same output!


# A dog named Willie.
describe_pet('willie')                 # Remember, "animal_type" has a default value.
describe_pet(pet_name='willie')
describe_pet(animal_type='dog', pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
# These are some equivalent ways!


# Finally, make sure you always meet the expected amount of arguments per function call to avoid argument errors!





##  PRACTICE STARTS NOW ##
""" Practice is currently starting now"""




# Lets create a function that it's job is to summarize and describe the size and the message printed on a shirt
def make_shirt(size, message_on_the_shirt):
    """Creating a prompt that describes and summarizing the size and the message printed on the shirt."""
    print(f"The shirt size is {size} and the message printed on the shirt is:  {message_on_the_shirt}.")

make_shirt('Small', 'Under Armour')
make_shirt(message_on_the_shirt='Adidas', size='Medium')




# Lets expand this function use and create a default value
def make_shirt(size='Large', message_on_the_shirt='I love Python'):
    """Creating a prompt that describes and summarizing the size and the message printed on the shirt."""
    print(f"The shirt size is {size} and the message printed on the shirt is:  {message_on_the_shirt}.")

make_shirt()
make_shirt('Medium')
make_shirt('Small', 'Python Rocks')




# Lets create another function that is about cities
def describe_city(city_name, name_of_country):
    """Stating the city name and which country is the city located."""
    print(f"{city_name} is inside the country of {name_of_country}!")

describe_city(city_name='Atlanta', name_of_country='United States of America')




# Lets expand this function to create default values and more function callings
def describe_city(city_name, name_of_country='India'):
    """Stating the city name and which country is the city located."""
    print(f"{city_name} is inside the country of {name_of_country}!")

describe_city('Mumbai')
describe_city(city_name='Hyderabad')
describe_city(name_of_country='Egypt', city_name='Cairo')
describe_city('Giza', 'Egypt')





###### END OF PRACTICE #######
""" This is the end of practice"""