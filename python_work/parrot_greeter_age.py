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