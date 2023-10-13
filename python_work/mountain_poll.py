# We can fill a dictionary with user input.
# Lets also do it with a while loop too!

# After the code is over, the code prints the results of the poll i'll create!
# Here is an example of a mountain poll:


responses = {}
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


# That is one example of how you do it.








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