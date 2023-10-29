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