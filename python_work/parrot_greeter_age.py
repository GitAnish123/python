# Lets learn how to accept user input! Here is an example,
message = input("Tell me something, and I will repeat it back to you!")
print(message)


# Lets write clear prompts
name = input("Please enter your name: ")
print(f"\nHello, {name}!")


# If you want to span two lines or more, do this:
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {prompt}!")


# Numerical values...
age = input("How old are you? ")
print(age)

age = input("How old are you? ")
"""  print(age >= 18),    This will cause an error"""

# Use the "int()" function to stop this
age = input("How old are you? ")
age = int(age)
print(age >= 18)  # That will result in a succesful conditional test!



# These examples above show how to write small, but interactive prompts!




# ----------- PRACTICE -------------- #
""" Practice now begins """

rental_car = input("What kind of rental car you need?")
rental_car = f"Let me see if I could find you a {rental_car}"
car = input(rental_car)


dining = input("How many people you have in your dinner group?")
dining = int(dining)

if dining >= 8:
   print("You would have to wait for some time to get a table.")
else:
    print("All right, your all set!")


determine_number = input("Enter a number and I will determine if it is a multiple of 10.")
number = int(determine_number)

if number % 10 == 0:
    print(f"The number, {number} is a multiple of 10!")
else:
    print(f"The number, {number} is NOT a multiple of 10!")

# --------- PRACTICE IS OVER ------------ #
""" PRACTICE IS CURRENTLY OVER!!! """


# While loops lessons!
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# Here is much more of a cleaner version and updates all bug fixes!!!

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# Lets keep a flag to support many events!
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
# That is useful for many complicated cases like games!
# It is very useful!


# ----------- PRACTICE -------------- #
""" Practice now begins """


pizza_prompt = "\nWe got your pizza ready but we are missing one more step. Enter 'quit' to stop the process."
pizza_prompt += "\nWhat toppings you want to add on your pizza: "

message = ""
while message != "quit":
    message = input(pizza_prompt)
    
    if message != "quit":
        print(f"We are adding {message}")


# 2nd example
movie_tickets = "\nToday we are releasing the old movie, Batman!"
movie_tickets += "\nEnter your age to go to the movie. Enter 'finished' to quit. Security passport check will be there."
movie_tickets += "\nWhat is your age in numeric form: "
while True:
    themovie = input(movie_tickets)
    if themovie == "finished":
        break
    else:
        themovie = int(themovie)
        if themovie <= 3:
            print("It is free to enter.")
        elif themovie <= 12:
            print("Ticket is $10 to enter.")
        else:
            print("Ticket is $15 to enter.")

# While conditioning examples
pizza_prompt = "\nWe got your pizza ready but we are missing one more step. Enter 'quit' to stop the process."
pizza_prompt += "\nWhat toppings you want to add on your pizza: "

message = ""
while message != "quit":
    message = input(pizza_prompt)
    
    if message != "quit":
        print(f"We are adding {message}")


movie_tickets = "\nToday we are releasing the old movie, Batman!"
movie_tickets += "\nEnter your age to go to the movie. Enter 'finished' to quit. Security passport check will be there."
movie_tickets += "\nWhat is your age in numeric form: "
message = ""
while message != "finished":
    message = input(movie_tickets)
    
    if message != "finished":
        message = int(message)
        if message <= 3:
            print("It is free to enter.")
        elif message <= 12:
            print("Ticket is $10 to enter.")
        else:
            print("Ticket is $15 to enter.")


# Flag examples
pizza_prompt = "\nWe got your pizza ready but we are missing one more step. Enter 'quit' to stop the process."
pizza_prompt += "\nWhat toppings you want to add on your pizza: "

active = True
while active:
    message = input(pizza_prompt)
    if message == "quit":
        active = False
    else:
        print(f"We are adding {message}")

movie_tickets = "\nToday we are releasing the old movie, Batman!"
movie_tickets += "\nEnter your age to go to the movie. Enter 'finished' to quit. Security passport check will be there."
movie_tickets += "\nWhat is your age in numeric form: "
active = True
while active:
    message = input(movie_tickets)
    if message == "finished":
        active = False
    else:
        message = int(message)
        if message <= 3:
            print("It is free to enter.")
        elif message <= 12:
            print("Ticket is $10 to enter.")
        else:
            print("Ticket is $15 to enter.")
        



# while "True" with a break value.
pizza_prompt = "\nWe got your pizza ready but we are missing one more step. Enter 'quit' to stop the process."
pizza_prompt += "\nWhat toppings you want to add on your pizza: "
while True:
    message = input(pizza_prompt)
    if message == "quit":
        break
    else:
        print(f"We are adding {message}")

movie_tickets = "\nToday we are releasing the old movie, Batman!"
movie_tickets += "\nEnter your age to go to the movie. Enter 'finished' to quit. Security passport check will be there."
movie_tickets += "\nWhat is your age in numeric form: "
while True:
    message = input(movie_tickets)
    if message == "finished":
        break
    else:
        message = int(message)
        if message <= 3:
            print("It is free to enter.")
        elif message <= 12:
            print("Ticket is $10 to enter.")
        else:
            print("Ticket is $15 to enter.")


# Here is a infinite loop!!!
while 1 == 1:
    print(True)



# --------- PRACTICE IS OVER ------------ #
""" PRACTICE IS CURRENTLY OVER!!! """




# Lets learn a example of how to define a function
# Here is a simple function...
def greet_user():
    """Display a simple greeting"""
    print("Hello")
greet_user()



# You also can pass information to a function!
# Lets provide a username so we can provide a greeting to a specific person's name!
# For example,

def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username}")
greet_user()
# That is some basic information of defining and passing information to a function.




# ----------- PRACTICE -------------- #
""" Practice now begins """




def display_message():
    """Display a message of what we learning"""
    print("We are learning about a block of code called functions")
display_message()                # We are calling/printing the function!




def favorite_book(title_of_book):
    """Display a message of your favorite books"""
    print(f"One of my favorite books is {title_of_book}")
favorite_book('Percy Jackson and the Olympians') # Calling the function with the argument and parameter of the favorite book!




# --------- PRACTICE IS OVER ------------ #
""" PRACTICE IS CURRENTLY OVER!!! """