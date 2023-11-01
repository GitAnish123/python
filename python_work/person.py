# You can return dictionaries inside of a function!
# For example:

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
# That is a simple example!


# You can also add more information like age, or occupation. You can add optional values so if you want you can include info
# Lets say for example, 'age'.
# For example,

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
# That is how you add multiple values and optional values.