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