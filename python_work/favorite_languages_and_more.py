python = "pythons"
print(python.title())
print("\tpython")
print("Languages:\nPython\nC\nJavascript")
print("kishan,\nHow are you?\nHope you are good!")
print("Hello\n\tKishan, your cracked at\tFortnite!\nHope you win\tThe next game\nHave fun:)")
favorite_language = ' python p'
print(favorite_language)
print(favorite_language.lstrip())
print(favorite_language)
favorite_language = f"{favorite_language.lstrip()}"
nostarch_url = 'https://nostarch.com'
print(nostarch_url)
print(nostarch_url.removeprefix('https://'))
print(nostarch_url)
nostarch_url = f"{nostarch_url.removeprefix('https://')}"
print(nostarch_url)
message = input("Hello, security challenge, Type anything and I will continue the program running!")
print(message)
# That is how you do "input" and "output"
# You can also use a dictinary to store one kind of info for many objects!
# For example,
favorite_language = {
    'jen':'python',
    'sarah':'C',
    'edward':'rust',
    'phil':'python',
}
# To use this dictionary, given the name of a person who took the poll, you can easily look up their favorite language:

favorite_language = {
    'jen':'python',
    'sarah':'C',
    'edward':'rust',
    'phil':'python',
}
language = favorite_language['sarah'].title()
print(language)
""" That is how you can use a dictinary. """
# You can apply these situations for other key-values in dictinary's!
# Lets loop all the key-value pairs.
# For exaample...

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
""" Now lets loop only the keys"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in favorite_languages.keys():
    print(name.title())
# Lets do an interesting example,


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
friends = ['sarah', 'phil']

for name in favorite_languages.keys():
   print(f"Hi {name.title()}.")
   if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# Another example

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

""" You might want to return a result of looping in a particular order.
Just simply use the "sorted() function.""" 
"""For example"""


favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for filling out the poll.")
for name in sorted(favorite_languages.keys(), reverse=True):
        print(f"{name.title()}, thank you for filling out the poll.")
# I printed it in alphabetical order and reverse alphabetical order.

""" This is how you loop all the values in a dictinary using the...
values() function."""
# For example,

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
# But if you want a unique code that has no repetition in it, you can use a set.
""" A set is a collection in which each item must be unique """
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# This is an example of how to build a set...
languages_in_a_set = {'python', 'rust', 'python', 'c'}
print(languages_in_a_set)
# What if you have more lists inside a dictinary:

# What if you have more lists?
""" Example??? """

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")