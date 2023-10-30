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