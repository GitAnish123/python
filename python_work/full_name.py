first_name = "anish"
last_name = "pasumarthi"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"hello, {full_name.title()}!")
message = f"hello, {full_name.title()}!"
print(message)





# In a function, you can return values to store for it later on!
# Lets do an example when we return a first and last name converting it into a neatly formatted name using "return"
# For example,

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('anish', 'pasumarthi')
print(musician)
# That is how you do a simple example of returning a function using "return".





# We can make an argument optional!
# For example, if we want to enter our first, middle, and last name, we can expand this code.
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# But middle names are not always needed!
# If you want to display your first and last name OR your first, middle, and last name, do this code!
# For example,

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
# That is an example of how you make an argument optional!



# You can also use "while" loops with functions
# Here is an example of a program that continuesly greets people
# For example, 
""" def get_formatted_name(first_name, last_name):
    ""Return a full name, neatly formatted.""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")  """


# The problem of the code is that, there is no quit condition, so it will keep on greeting people.
# Here is the better version that will apply quit conditions along with the simple examples that contains first & last names.
# For example,
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
# That is an example of while loops with functions
# Make sure when you do while loops, always make sure to apply a quit condition so it doesn't run forever!