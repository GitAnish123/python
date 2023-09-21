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